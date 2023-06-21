//replace worldmodel with 'worldmodel'
//receive message from openai, vector db; send it to server, display from server
//or receive message from openai, display from here; send it to server, vector db
//vectordb = append to csv file
 
function replace(){
    console.log('replaced!')
    document.getElementsById('world-model').innerText = "hello world";
}

document.getElementById("btn").addEventListener("click",replace());