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
