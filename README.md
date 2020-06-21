# 排行榜服务

##本服务现有两个接口分别是：
   ### 接口1
   http://127.0.0.1:8000/user/fractionupload/ <br>
   使用方法：<br>
   使用postman发送post请求 修改body中form-data(name-->5,fraction-->111111)
   ##### 成功返回:<br>
   {
           "message": "success"
       }<br>
   #####失败返回：<br>
   { "message": "fail" }
   ### 接口2
   http://127.0.0.1:8000/user/fractionquery/<br>
   使用方法：<br>
   使用postman发送post请求 修改body中:<br>form-data(name-->11)或者(name-->11,startname-->0,stopname-->10)
   返回如下json数组<br>
   <p>{
         "Rank": {
             "0": 1,
             "1": 2,
             "2": 3,
             "3": 4,
             "4": 5,
             "5": 6,
             "6": 7,
             "7": 9,
             "8": 9,
             "9": 10,
             "10": 1
         },
         "name": {
             "0": "11",
             "1": "1",
             "2": "2",
             "3": "3",
             "4": "4",
             "5": "6",
             "6": "5",
             "7": "7",
             "8": "8",
             "9": "9",
             "10": "11"
         },
         "fraction": {
             "0": 99999988,
             "1": 9999999,
             "2": 9500112,
             "3": 9233333,
             "4": 5445444,
             "5": 2342342,
             "6": 111111,
             "7": 66666,
             "8": 66666,
             "9": 76,
             "10": 99999988
         }
     }</p>
   