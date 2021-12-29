`DXF` 矢量图: 图框提取
======================================


粗效果
^^^^^^^^^

- 假设拥有 `dxf` 图纸，大致内容如下：


.. figure:: /_static/pics/dxf_a3s.png

   图纸预览效果

- 基于实体包围框融合

.. figure:: /_static/pics/dxf_bounding_box.png

   包围框融合后预览

- 分类提取格式转换

.. figure:: /_static/pics/dxf_split_to_pic.png

   基于包围框分割提取存放

往后加上一个单层神经网络，做图片的二分类（图纸 or not 图纸），就基本完成图框提取，可以为后续流程做铺垫。
