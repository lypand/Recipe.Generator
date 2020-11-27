function loadDoc() {
    fetch('http://pokeapi.co/api/v2/pokemon/25/')
  .then(response => response.json())
  .then(data =>   
    
    {
        document.getElementById("h1").innerHTML = data.species.name; 
        document.getElementById("img1").src = data.sprites.front_shiny; 
        console.log(data); 
    });


  }







