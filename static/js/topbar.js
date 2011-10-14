var shortlist_ids = [];

var submitter = function(action, list_name, list_value) {
	var form = document.createElement("form");
	form.setAttribute("method", "POST");
	form.setAttribute("action", action);

	var hidden = document.createElement('input');
	hidden.setAttribute("type", "hidden");
	hidden.setAttribute("name", list_name);
	hidden.setAttribute("value", list_value);
	form.appendChild(hidden);

	var csrf = document.createElement('input');
	csrf.setAttribute("type", "hidden");
	csrf.setAttribute("name", "csrfmiddlewaretoken");
	csrf.setAttribute("value", csrf_token);	
	form.appendChild(csrf);
	
	form.submit();
};

$(window).load(function () {
	// Adding the number of shortlist elements to it's link
	if ($.cookie('shortlist_ids') != null) {
		shortlist_ids = $.parseJSON($.cookie('shortlist_ids'));
	}

	$('div.shortlist-link a').append('(' + shortlist_ids.length + ')' + ' &gt;');
	$('a.shortlist-link').append('(' + shortlist_ids.length + ')' + ' &gt;');

	// Adding the shortlist submission function
	$('.shortlist-link').each(function () {
		$(this).click(function () {
			submitter("/" + curr_lang_code + "/search/","shortlist_ids","[" + shortlist_ids.join(', ') + "]");
		});
	});
});