$(document).ready(function () {
    $('#dataTable').DataTable(
        {
            drawCallback: function(){
                $("img.lazy").lazyload();
            }
        }
    /*    {"columns": [
        { "width": "10%" },
        { "width": "10%" },
        null,
        { "width": "20%" },
      ]
    }*/
    );

    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

});
