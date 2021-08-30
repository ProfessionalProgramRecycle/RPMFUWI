# RPMFUWI
这是一个专为辽宁工业大学-众智创新团队的EES电梯模拟程序所建立的客流模型创建程序。<br/>
This is a passenger flow creation program designed for the elevator operation simulation program of The Research Group of Unity Wisdom Innovation.

### Default parameters：

完全随机客流，限制int(1||2||3)，<br/>
三部电梯，限制int(1||2||3||6)，<br/>
每梯十层，限制int(6||10)，<br/>
初始化到达最高层，限制int([1,10]||[1,6])，<br/>
向上初始化，限制int(1||2)，<br/>
初始化默认撞击第一限位，不撞击第二限位，限制int(0||1)，<br/>
乘梯数200人，限制int([1,1000])，<br/>
初始化限制时间100S，限制int([50,200])，<br/>
首位乘客出现时间晚于初始化限制时间+1，限制int([初始化限制时间+1,∞))，<br/>
末位乘客出现时间早于首位时间+每位平均0.05S，限制int([首位时间+每位平均0.05S,∞))，<br/>
乘客重量最重90KG，限制int([60,120])，<br/>
乘客重量最轻30KG，限制int([16,40])，<br/>
强制判分时间为末位乘客出现后60S，限制int(末位乘客出现时间+[30S,1000S])。<br/>

