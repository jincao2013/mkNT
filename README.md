# About mkNT #

mkNT is a python based program producing initial structure of different size of nano-tubes from its 2D-sheet of material. 

## How to use ##

1.	mkNT can only process standard VASP POSCAR file. Rename your POSCAR file of prime cell to POSCAR_unit and placed with mkNT.py in the same folder.   
	1)	ensuring POSCAR_unit is orthorhombic prime cell  
	2)	ensuring 'c' is the normal diraction of 2D_sheet, mkNT will rolls around 'a' axil of 2D_sheet following the rule of right hand.  
	3)	atoms should formate a 2D_sheet, but not via periodic bountary condition,  i.e. atoms should not cross the bountary, if you get a result with a strangely large R, it may cause from this.  
2.	Input parametes in run_me.py as your demand, which include input_filename, A, C, vacuum_list, B_list.  
	1)	input_filename：file name of 2D_sheet，default to 'POSCAR_unit'  
	2)	A：build a A times large supercell along a axis before rolling  
	3)	C：build a C times large supercell along c axis before rolling  
	4)	vacuum_list：vacuum_list is a list，the numbers in the list controls interval between nano-tubes    
	5)	B_list：B_list is a list，the numbers in the list decide that B periods exist along circle direction.  
	6)	vacuum_list and B_list include lots of parametes (see example below)，mkNT will produce many POSCAR files of nano-tube according to your parametes.  
3.	run_me.py  
	1)	python run_me.py  

## Example of input of run_me.py ##

	############## input ##############
	input_filename = 'POSCAR_unit'
	A = 1
	C = 1
	vacuum_list = [10,15,20]
	B_list = [8,9,10,11,12,13,14,15,16,17,18,19,20]
	############## input ##############

In this example of input of run_me.py, a sets of nano-tube, which inclued [8,9,10,11,12,13,14,15,16,17,18,19,20] times large of supercell with [10,15,20] angstrom of intercal, were produced from 2D-sheet that described by POSCAR_unit.

## mkNT were used in Works of following paper ##

1. Jin Cao, Jing Shi, Musheng Wu, Chuying Ouyang, Bo Xu. Lithium ion adsorption and diffusion on black phosphorene nanotube: A first-principles study. *Applied Surface Science* **392**, 88–94 (2017). [Link](http://dx.doi.org/10.1016/j.apsusc.2016.09.004 "DOI")


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

## mkNT 在下面的工作中被用到 ##

1. Jin Cao, Jing Shi, Musheng Wu, Chuying Ouyang, Bo Xu. Lithium ion adsorption and diffusion on black phosphorene nanotube: A first-principles study. *Applied Surface Science* **392**, 88–94 (2017). [链接](http://dx.doi.org/10.1016/j.apsusc.2016.09.004 "DOI")
