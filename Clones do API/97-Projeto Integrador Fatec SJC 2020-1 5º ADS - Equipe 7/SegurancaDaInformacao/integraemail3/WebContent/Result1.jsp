<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>

<style>
*{
	margin:0;
	padding:0;
}

#bg{
	width:100%;
	height:100%;
	top:0;
	left:0;
	background-color: rgba(0,0,0,.8);
	position: fixed;
	display:none;
}

#bg:target{
	display: block;
}
#bg:target ~ .box{
	top:150px;
	transition: all .3s;
	transition-delay: .2s;
}

.box{
	width: 720px;
	height:405px;
	position: absolute;
	margin-left: -360px;
	left:50%;
	background-image: url("grey_back.jpg");
	top:-410px;
}

#im{
	top:3;
}

#message{
	color: black;
	font-family: 'Arial';
	text-decoration: none;
	font-size: 20px;
}

.bt {
  background-color: #555555;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}


#close{
	color: #fff;
	font-family: 'Arial';
	text-decoration: none;
	font-size: 20px;
	position: absolute;
	background-color: red;
	width:7%;
	height:7%;
	text-align: center;
	right: 0;
	top:0;
}

#close: hover{
	opacity: .6;
}

</style>

</head>
<body>

<a href="#bg">Pop-Up</a>

<div id="bg"> </div>
<div class="box">
	<br/>
	<div id="im" align="center" ><img src="assets/mail.png" width="200px" height="200px"></div>
	<a href="" id="close">X</a>
	<br/>
	<div id="message" align="center"> <p>Acabamos de enviar um email com o resumo simples contendo todas as informações sobre o uso de seus dados.</p>
	<br/>
	<a href=""><button class="bt">Fechar</button></a>
	</div>
</div>

</body>
</html>