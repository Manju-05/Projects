const taskInput = document.getElementById("taskInput");
const taskList  = document.getElementById("listItems");

function addTask() {
    const taskText = taskInput.value.trim();

    if(taskText == ""){
        alert("Can't add Empty!! please add the Task")
    }
    else{
        const listItem = document.createElement("li");

        listItem.innerHTML = `${taskText}
        <button onclick = "deleteTask(this)" class="del">Delete</button>  ` ,  
        taskList.appendChild(listItem)
        taskInput.value = "";
    }  
}

function deleteTask(button) {
    const listItem = button.parentElement;
    taskList.removeChild(listItem); 
}