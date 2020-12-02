function loadDoc() {
   fetch('http://127.0.0.1:5000/data',{
    //	mode: 'no-cors'
    })
  .then(response => response.json())
  	

  	.then(data =>   
    
    {
        console.log(data); 
        document.getElementById("h1").innerHTML = data.name; 
        document.getElementById("img1").src = data.image.url; 
        
    });


  }



/*var request = new XMLHttpRequest();
  	request.open('GET','http://127.0.0.1:5000/data',{
  		mode:'no-cors'
  	});
	request.responseType = 'json';
	console.log(request.send());
	        console.log(request.response); */



