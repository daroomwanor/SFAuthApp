function get_connected_app(){
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			window.location.href = this.responseText;
			console(this.responseText);
		}

	};
	xmlhttp.open("POST", "http://darrigoldgroup.com:5000/get_connected_app_url");
	xmlhttp.send();
}

function get_instance_url(e){
	var url = e.getAttribute("data-record");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		document.getElementById('id01').style.display='block';
		document.getElementById('id01_container').innerHTML = this.responseText;
	};
	xmlhttp.open("GET", "http://darrigoldgroup.com:5000/get_org_details?url="+url);
	xmlhttp.send();
}


function enable_org(){
	var url = document.getElementById('url').value;
	var action = document.getElementById('action').value;
	if(action != ""){
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200){
				console.log(this.responseText);
			}
			
		};
		xmlhttp.open("GET", "http://darrigoldgroup.com:5000/enable_org?url="+url+"&action="+action);
		xmlhttp.send();
	}
}


function pushBack(e){
	var Id = e.getAttribute("data-record");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			document.getElementById('id01').style.display='block';
			document.getElementById('id01_container').innerHTML = "Contact with Id "+Id+" has been updated in your Salesforce Org";
		}
	};
	xmlhttp.open("GET", "http://localhost:5000/pushBack?Id="+Id);
	xmlhttp.send();
}