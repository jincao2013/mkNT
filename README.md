# mkNT 使用说明 #

mkNT用于把层状的材料卷成不同口径的纳米管

## 使用说明 ##

1.	把原胞的POSCAR重命名为POSCAR_unit，并与mkNT.py在同一文件夹下。  
  1)	注意：原胞必须是正交的胞  
  2)	注意：确保c方向是层状材料的法向，程序会沿a方向按照右手定则确定如何生成纳米管  
  3)	整个层状材料的结构应当连续的出现在原胞内，而不是通过周期性边界条件  
2.	在run_me.py的input里面按需求输入input_filename, A, C, vacuum_list, B_list  
  1)	input_filename：输入的层状材料的原胞的文件名，默认为POSCAR_unit  
  2)	A：沿a方向扩胞A倍  
  3)	C：沿c方向扩胞C倍  
  4)	vacuum_list：vacuum_list是一个列表，列表中的数字控制了圈好的纳米管之间的间距  
  5)	B_list：B_list是一个列表，列表中的数字控制了纳米管沿圆周方向有B个周期  
  6)	vacuum_list和B_list可输入多个数值（实例如下），程序将分别输入不同要求的纳米管  
3.	运行run_me.py  
  1)	python run_me.py  

## run_me.py的input示例 ##

	############## input ##############
	input_filename = 'POSCAR_unit'
	A = 1
	C = 1
	vacuum_list = [10,15,20]
	B_list = [8,9,10,11,12,13,14,15,16,17,18,19,20]
	############## input ##############

这个示例将POSCAR_unit描述的层状材料的原胞沿B方向分别扩胞[8,9,10,11,12,13,14,15,16,17,18,19,20]倍后输出含[10,15,20]埃的真空层的纳米管

