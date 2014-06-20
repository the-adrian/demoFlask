      $(document).ready(function(){
        $('#btncalcular').click(function(){
          if($("#fechaInicio").val().length < 1 || $("#fechaFin").val().length<1){
            alert("Introduce los valores correspondientes al inicio y fin de la consulta");
          return $("#fechaFin").val(""), $("#fechaInicio").val("");;
        }
        });
      });
     
