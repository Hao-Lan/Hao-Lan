模型生成点云
============

==============  =============
 Create
 Last Update     2021-12-29
==============  =============


通过 `pythonocc-core` 读取 `ifc` 文件，点云化

.. figure:: /_static/pics/point_could_2021_12_8.png

   点云填充效果图

.. code-block:: python
   :name: pythonocc-core 和 ifcopenshell 示例
   :caption: Block caption
   :linenos:

    import math
    import random
    from typing import Iterable, List

    import numpy as np
    import ifcopenshell
    from ifcopenshell import geom
    from OCC.Core.gp import gp_Pnt
    from OCC.Core.BRep import BRep_Tool
    from OCC.Core.Poly import Poly_Triangle
    from OCC.Core.TopLoc import TopLoc_Location
    from OCC.Core.TopExp import TopExp_Explorer
    from OCC.Core.GeomAbs import (GeomAbs_Plane)
    from OCC.Core.TopAbs import TopAbs_ShapeEnum
    from ifcopenshell.file import file as IfcFile
    from OCC.Display.SimpleGui import init_display
    from OCC.Core.BRepAdaptor import BRepAdaptor_Surface
    from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
    from OCC.Extend.ShapeFactory import make_edge, make_vertex
    from OCC.Core.TopoDS import topods_Face, TopoDS_Shape, TopoDS_Face


    def gp_pnt_2_np(pnt: gp_Pnt) -> np.ndarray:
        return np.asarray([pnt.X(), pnt.Y(), pnt.Z()])


    def filling_pnt(v1: gp_Pnt, v2: gp_Pnt, v3: gp_Pnt, nums: int = 10) -> Iterable[np.ndarray]:
        v1 = gp_pnt_2_np(v1)
        v2 = gp_pnt_2_np(v2)
        v3 = gp_pnt_2_np(v3)

        for _ in range(nums):
            r1 = random.random()
            r2 = random.random()
            mid = math.sqrt(r1)
            a = 1 - mid
            b = mid * (1 - r2)
            c = mid * r2
            yield a * v1 + b * v2 + c * v3


    def triangle_area(triangle: List[gp_Pnt]) -> float:
        distance_a = triangle[0].Distance(triangle[1])
        distance_b = triangle[0].Distance(triangle[2])
        distance_c = triangle[1].Distance(triangle[2])
        p = (distance_a + distance_b + distance_c) / 2
        area = math.sqrt(p * (p - distance_a) * (p - distance_b) * (p - distance_c))
        return area


    def create_triangles(shape: TopoDS_Shape) -> List[List[gp_Pnt]]:
        _triangles: List[List[gp_Pnt]] = []
        BRepMesh_IncrementalMesh(shape, 0.8)
        bt = BRep_Tool()
        ex = TopExp_Explorer(shape, TopAbs_ShapeEnum.TopAbs_FACE)
        while ex.More():
            face: TopoDS_Face = topods_Face(ex.Current())
            surf = BRepAdaptor_Surface(face, True)
            surf_type = surf.GetType()
            if surf_type == GeomAbs_Plane:
                gp_pln = surf.Plane()
                normal = gp_pln.Axis().Direction()  # the plane normal
            else:
                raise Exception("error else ")

            location = TopLoc_Location()
            facing = (bt.Triangulation(face, location))

            trans_form = face.Location().Transformation()
            tab = facing.Nodes()
            tri = facing.Triangles()
            for i in range(1, facing.NbTriangles() + 1):
                train: Poly_Triangle = tri.Value(i)
                index1, index2, index3 = train.Get()
                _triangles.append([
                    tab.Value(index1).Transformed(trans_form),
                    tab.Value(index2).Transformed(trans_form),
                    tab.Value(index3).Transformed(trans_form),
                    gp_Pnt(normal.XYZ()),
                ])
            ex.Next()
        return _triangles


    def main():
        show = True  # 是否在生成的过程中显示点填充效果
        density_factor = 1  # 修改来改变填充的密度,和面积数值相关,和单位相关,需要人为调整
        step_show = True

        display, start_display, add_menu, add_function_to_menu = init_display()

        settings = geom.settings()
        # Use python occ-core
        settings.set(settings.USE_PYTHON_OPENCASCADE, True)

        ifc_file: IfcFile = ifcopenshell.open("out7-1.ifc")
        with open("points.xyz", "w") as points_f:
            for i, product in enumerate(ifc_file.by_type("IfcProduct")):
                if product.Representation is not None:  # some IfcProducts don't have any 3d representation
                    try:
                        product_shape = ifcopenshell.geom.create_shape(settings, inst=product)
                    except RuntimeError:
                        print("Failed to process shape geometry")
                    else:
                        # success
                        shape = product_shape.geometry
                        triangles = create_triangles(shape)
                        for triangle in triangles:
                            area_tmp = triangle_area(triangle)
                            nums = int(area_tmp * density_factor) or 1  # 最少一个点
                            print(f"面积:{area_tmp},点数:{nums}")
                            if nums > 0:
                                for pnt in filling_pnt(triangle[0], triangle[1], triangle[2], nums):
                                    pnt_list: List = list(pnt)
                                    pnt_list.extend([triangle[-1].X(), triangle[-1].Y(), triangle[-1].Z()])
                                    line = " ".join(map(str, pnt_list)) + "\r"
                                    points_f.write(line)
                                    if show:
                                        vertex = make_vertex(gp_Pnt(*list(pnt)))
                                        display.DisplayShape(vertex)  # 可以不用显示
                                if show:
                                    edg_1 = make_edge(triangle[0], triangle[1])
                                    edg_2 = make_edge(triangle[1], triangle[2])
                                    edg_3 = make_edge(triangle[2], triangle[1])
                                    # 可以不用显示
                                    display.DisplayShape(edg_1)
                                    display.DisplayShape(edg_2)
                                    display.DisplayShape(edg_3, update=step_show)
                            else:
                                print(f"密度系数导致三角形未生成点数据")
        if show:
            start_display()


    if __name__ == '__main__':
        main()
