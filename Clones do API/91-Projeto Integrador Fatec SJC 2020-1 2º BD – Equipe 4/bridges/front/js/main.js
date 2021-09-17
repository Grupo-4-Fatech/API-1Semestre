$(document).ready(function() {
  $('.table').DataTable( {
      "language": {
          "lengthMenu": "Mostrar _MENU_ registros por página",
          "zeroRecords": "Nenhum registro encontrado",
          "info": "Mostrando página _PAGE_ de _PAGES_",
          "search": "Buscar",
          "infoEmpty": "Nenhum registro encontrado",
          "infoFiltered": "(Filtrados de _MAX_ registros)",
          "paginate": {
          "first":      "Primeira",
          "last":       "Última",
          "next":       "Próxima",
          "previous":   "Anterior",
          
        },
      }
  } );
} );


$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	var actions = $("table td:last-child").html();
	// Append table with add row form on add new button click
    $(".add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="text" class="form-control" name="name" id="name"></td>' +
            '<td><input type="text" class="form-control" name="department" id="department"></td>' +
            '<td><input type="text" class="form-control" name="phone" id="phone"></td>' +
			'<td>' + actions + '</td>' +
        '</tr>';
    	$("table").append(row);		
		$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
	// Add row on add button click
	$(document).on("click", ".add", function(){
		var empty = false;
		var input = $(this).parents("tr").find('input[type="text"]');
        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		$(this).parents("tr").find(".error").first().focus();
		if(!empty){
			input.each(function(){
				$(this).parent("td").html($(this).val());
			});			
			$(this).parents("tr").find(".add, .edit").toggle();
			$(".add-new").removeAttr("disabled");
		}		
    });
	// Edit row on edit button click
	$(document).on("click", ".edit", function(){		
        $(this).parents("tr").find("td:not(:last-child)").each(function(){
			$(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
		});		
		$(this).parents("tr").find(".add, .edit").toggle();
		$(".add-new").attr("disabled", "disabled");
    });
	// Delete row on delete button click
	$(document).on("click", ".delete", function(){
        $(this).parents("tr").remove();
		$(".add-new").removeAttr("disabled");
    });
});


$('.btn').click(function Login() {
  var usuario = document.getElementById('usuario').value;
  var senha= document.getElementById('senha').value;
  if (usuario =="admin" && senha =="admin") {
    window.location="main.html";
  }
  else {alert("Dados incorretos, tente novamente!")}
} );

// Pegar o campo de input
var input = document.getElementById("senha");
// Executar a função quando o usuario apertar uma tecla do teclado
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    // Acionar o botão enter
    document.getElementById("login").click();
  }
});





/*$(document).ready(function() {
var table = $('.table').DataTable();

new $.fn.dataTable.Buttons( table, {
    buttons: [
  {
    'extend': 'print',
    'text': function ( dt, button, config ) {
      return dt.i18n( 'buttons.print', 'Imprimir' );
    }
    
  }            
    ]
} );

table.buttons( 0, null ).container().prependTo(
    table.table().container()
)
} );*/

