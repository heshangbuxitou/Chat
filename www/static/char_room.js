var maxID = 0;

		function showMsg() {
			var xhr = new XMLHttpRequest();
			var div = document.getElementById('top');
			// var msg = document.getElementById('msg');
			xhr.onreadystatechange = function() {
				if(xhr.readyState == 4) {

					eval("var json_info="+xhr.responseText);
					// var p = document.createElement('p');
					// p.innerHTML = xhr.responseText;

					// div.appendChild(p);
					var s = "";
					for(var i = 0; i < json_info.length; i ++) {
						s += "<tr><td class='td_username'><font color='red'>"+ json_info[i].username+"&nbsp;&nbsp;&nbsp;</font></td>:<td class='td_msg'><font color='#000'>&nbsp;&nbsp;&nbsp;"+json_info[i].content+"</font></td></tr><br>";
						maxID = json_info[i].id;
					}
					div.innerHTML += s;

					div.scrollTop = div.scrollHeight;

					// alert("fdsfd");
				}
			}
			// xhr.open('get', 'abc.php?msg='+msg.value);
			xhr.open('get', '/chat?maxID='+maxID,false);
			xhr.send(null);
		}
		window.onload = function() {
			setInterval("showMsg()", 2000);
		}	
 	
		function clickButton() {
 			// var msg = document.getElementById('msg');
 			// alert(msg.value);
 			var msg = document.getElementById('msg');
 			var m = msg.value;
 			msg.value = '';

 			var xhr = new XMLHttpRequest();
			var div = document.getElementById('top');
			// var msg = document.getElementById('msg');
			xhr.onreadystatechange = function() {
				if(xhr.readyState == 4) {

					// var p = document.createElement('p');
					// p.innerHTML = xhr.responseText;

					// div.appendChild(p);
					div.scrollTop = div.scrollHeight;

					

				}
			}
			var username = document.getElementById('username_id').innerHTML;
			// id = getId(id);
			var url = '/chat?m=' + m + '&username=' + username;
			xhr.open('get', url,false);
			// xhr.open('get', 'abc.php?m=');
			xhr.send(null);

 		}

 		document.onkeydown=function(event){
            var e = event || window.event || arguments.callee.caller.arguments[0];

             if(e && e.keyCode==13){ 
				clickButton();
            }
        }; 