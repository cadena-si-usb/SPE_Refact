(function(){

$('#sedesIndex').ready(function(){
    var ajaxHandler = AjaxHandler();

    var sede = [],
        max, area, options = {},
        filters = {order:'id',side:'>',limit:'4',page:'0'},
        filter = {},
        search = {};

    function activate(){
        getInfo();
    }

    activate();

    function getInfo(){
        options = {};

        if (filters.page && filters.page != "") {
            filters.page = "0";
        }

        options.data = $.param(filters,true);

        ajaxHandler.count('sedes',options).success(function(res){
            max = res;
            $('#cantidad').html(max.toString());
            getMaterias();
        })
    }

    function getMaterias(){
        ajaxHandler.find('sedes',options).success(function(res){
            sede = JSON.parse(res);
            if (sede.length > 0){
                $("#elBody").loadTemplate('#template', sede);
            }
            else {
                var template = '<tr><td class="text-center" colspan="42">',
                    msg = "No hay elementos en la tabla";

                template += msg + "</td></tr>";

                $("#elBody").html(template);
            }

            disableButtonOnMax();
        });
    }

    // Cambiar orden de los elementos

    function changeOrder(evt){
        var order = this.id,
            side = filters.side,
            current = filters.order;

        if (order != current){
            filters.order = order;
            filters.side = '>'
        }
        else {
            if (filters.side === '>') {
                filters.side = '<'
            }
            else {
                filters.side = '>'
            }
            filters.order = order;
        }

        setCaret($(this));

        getInfo();
    }

    function setCaret(elem){
        var isOrdered = $('#orderBy').length,
            caret;

        if (isOrdered){
            $('#orderBy').remove();
        }

        if (filters.side === ">"){
            caret = "down"
        }
        else {
            caret = "up"
        }

        var fa = "fa fa-caret-square-o-" + caret
        elem.append(" <i id='orderBy' class='"+ fa +"'></i>")
    }

    // Funcion que trae mas sede para paginacion

    function getMoreMaterias(evt){
        filters.page = sede.length.toString();

        options.data = $.param(filters,true);
        //AJAX CALL TO SERVER
        ajaxHandler.find('sedes',options).success(function(res){
            res = JSON.parse(res);
            for (var i = 0; i < res.length; i++){
                sede.push(res[i]);
            }
            disableButtonOnMax();

            $("#elBody").loadTemplate('#template',res,{append:true});
        });
    }

    //Desabilitar boton de MAS

    function disableButtonOnMax(){
        if ((max) && (sede.length.toString() != max)) {
            $("#next").prop('disabled',false);
        }
        else {
            $("#next").prop('disabled',true);
        }
    }

    //Buscador

    function searchTerm(evt){
        var delay = (function(){
            var timer = 0;
            return function(callback, ms){
            clearTimeout(timer);
            timer = setTimeout(callback, ms);
            };
        })();

        var val = this.value,
            ms = 200;

        delay(function(){
            if (val){
                search["key"] = "first_name"
                search["value"] = val;
            } else {
                search = {}
            }

            filters.searchTerm = JSON.stringify(search);

            getInfo();
        }, ms);
    }


    $('#search').keyup(searchTerm);
    $('#next').click(getMoreMaterias);
    $('.uai-table-header').click(changeOrder);
});
})();
