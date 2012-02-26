function initMenu() {
    $('#menu ul').hide(); // Hide the submenu
    if ($('#menu li').has('ul')) {
	$('#menu ul').prev().addClass('expandable'); // Expand/collapse a submenu when it exists
    }
    $('.expandable').click(
	function() {
	    $(this).next().slideToggle();
	    $(this).toggleClass('expanded');
	}
    );
}
// When document ready, call initMenu() function
$(document).ready(function() {initMenu();});


//ajax search
$(document).ready(function() {
		      $( ".ui-autocomplete-input" ).autocomplete({
						    source: function( request, response ) {
							$.ajax({
								   url: "/bpg/asearch/",
								   dataType: "jsonp",
								   data: {
								       name: "Monty",
								       food: "Spam" 
								       // featureClass: "P",
								       // style: "full",
								       // maxRows: 12,
								       // name_startsWith: request.term
								   },
								   success: function( data ) {
								       response( $.map( data.geonames, function( item ) {
											    return {
												label: item.name + (item.adminName1 ? ", " + item.adminName1 : "") + ", " + item.countryName,
												value: item.name
											    }
											}));
								   }
							       });
						    },
						    minLength: 2,
						    select: function( event, ui ) {
							log( ui.item ?
							     "Selected: " + ui.item.label :
							     "Nothing selected, input was " + this.value);
						    },
						    open: function() {
							$( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
						    },
						    close: function() {
							$( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
						    }
						});
		  });

