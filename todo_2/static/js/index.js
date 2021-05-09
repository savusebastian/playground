$(document).ready(function(){
    $('.chartWrapper').insertAfter('h1');
});


// Vue
var listItems = document.getElementsByClassName('list-group-item');
var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        searchInput: '',
        taskInput: '',
        search_locationInput: '',
    },
    methods: {
        searchFilter(value){
            for (var i = 0; i < listItems.length; i++) {
                listItems[i].classList.remove('nada');
                // console.log(listItems[i].getElementsByTagName('p')[0].textContent.search(this.searchInput));

                if(listItems[i].getElementsByTagName('p')[0].textContent.search(this.searchInput) == -1){
                    listItems[i].classList.add('nada');
                }
            }
        }
    }
});
