document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {

    // Initialize new request
        const request = new XMLHttpRequest();
        const book = document.querySelector('#book').value;
        request.open('POST', '/bookinfo');

    // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result table
            if (data.success) {
                let i;
                let n = data.items.length;
                var txt = ``;
                for (i = 0; i < n; i++) {
                    txt += `<tr><td> ${data.items[i].volumeInfo.title} </td></tr>`;
                    txt += `<tr><td> ${data.items[i].volumeInfo.authors} </td></tr>`;
                    txt += `<tr><td> ${data.items[i].volumeInfo.publisher} </td></tr>`;
                    txt += `<tr><td> <img src=${data.items[i].volumeInfo.imageLinks.thumbnail}> </td></tr>`;
                    txt += `<tr><td> <a href=${data.items[i].volumeInfo.canonicalVolumeLink}>More Info</a> </td></tr>`;
                    document.querySelector('#result').innerHTML = txt;                    
                }                
            }
            else {
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }
        
        // Add data to send with request
        const data = new FormData();
        data.append('book', book);

        // Send request
        request.send(data);
        return false;
    };

});
