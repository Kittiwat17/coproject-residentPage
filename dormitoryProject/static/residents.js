function CheckCost(){
    document.getElementById('resident-content').innerHTML = '';
    axios.get('CheckCost/', {

    })
    .then(function(response){
        // respones.data.inv_id.forEach(item => {
        //     console.log(respones.data.inv_id);
        // });
        var i = 0
        while(true){
            if(response.data[i] && response.data[i][0]){
                createTextBox('Contract ID : '+i,'resident-content');
                response.data[i].forEach(invoice => {
                    createBilBox(invoice.id, invoice.inv_date);
                });
                i += 1;
            }
            else{
                break;
            }
        }
        // createBilBox(response)
        console.log(response);
    })
    .catch(function(error){
        console.log(error);
    });
}

function createBilBox(id, date){
    let contentBox = document.getElementById('resident-content');

    let box = document.createElement('div');
    let bilText = document.createTextNode('invoice ID : '+id+' date : '+date);

    box.className = 'bilBox bg-light rounded';
    box.appendChild(bilText);

    contentBox.appendChild(box);
}

function createTextBox(text, addtoID){
    let contentBox = document.getElementById(''+addtoID);

    let box = document.createElement('div');
    let bilText = document.createTextNode(text);

    box.className = 'textBox bg-light';
    box.appendChild(bilText);

    contentBox.appendChild(box);
}

function Comments(){
    console.log("q");
}