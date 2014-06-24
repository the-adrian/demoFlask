      $(document).ready(function(){
        $('#btncalcular').click(function(){
          if($("#fechaInicio").val().length < 1 || $("#fechaFin").val().length < 1){
            alert("Introduce los valores correspondientes al inicio y fin de la consulta");
          return $("#fechaFin").val(""), $("#fechaInicio").val("");
        }
        });
      });

         $(document).ready(function(){
        $('#btncalcular').click(function(){
          if($("#fechaInicio").val().length > 0 || $("#fechaFin").val().length < 0){
            alert("consulta valida");
        }
        });
      });
     
     
function visualizacionCapas(capa){
	if(capa=="")
	{
		capa="Administracion"
	}
	$("article#"+capa).addClass("active");
}