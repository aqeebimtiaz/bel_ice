$(document).ready(function(){
    $('#saleForm').submit(function(event) {
        let saleRawData = $('#shop_sale_details');
        console.log(saleRawData.val());
        data = {
            data : saleRawData,
            type : 'json'
        }
        console.log(data)
        $.ajax(
            {
                type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
                url         : '/ice-new', // the url where we want to POST
                data        : data, // our data object
                dataType    : 'application/csv', // what type of data do we expect back from the server
                // encode      : true

                success: function (data) {
                    csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(data);
                    $("#exportsags").attr({
                        "href": csvData,
                        "download": "sag_data.csv"
                    });
                }
            },

        )

        event.preventDefault();
    });
});

