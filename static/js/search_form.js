var curr_min_price;
var curr_max_price;
var curr_min_bedroom;
var curr_max_bedroom;
var curr_sale_type;

/* Populating the selectors START */

function show_hide_options (options, values, texts) {
	for(var i = 0; i < options.length; i++) {
		if(i < values.length) {
			$(options[i]).attr('value', values[i]);
			$(options[i]).text(texts[i]);
			$(options[i]).show();
		} else {
			$(options[i]).hide();
			$(options[i]).attr('value', -1);
		}
	}
}

function reset_sales_options (type) {
	var pricelist;
	curr_min_price = 0;
	curr_max_price = 99999999999;
	
	if(type == "rentals") {
		pricelist = rentals_prices;
	} else { // type == "sales"
		pricelist = sales_prices;
	}

	// Adding prices to the minimum price selector.
	var options = $('select#min_price-select option');
	var values = [0].concat(pricelist.slice(0,pricelist.length - 1));
	var texts = [min_text].concat(pricelist.slice(0,pricelist.length - 1));
	show_hide_options(options, values, texts);
	for(var i = 0; i < options.length; i++) {
		if(i == 0) {
			$(options[i]).attr('selected', 'selected');
		} else {
			$(options[i]).removeAttr('selected');
		}
	}


	// Adding prices to the maximum price selector.
	options = $('select#max_price-select option');
	values = [99999999999].concat(pricelist.slice(1,pricelist.length));
	values[values.length - 1] = 99999999999;
	texts = [max_text].concat(pricelist.slice(1,pricelist.length));
	texts[texts.length - 1] = texts[texts.length - 1] + '+';
	show_hide_options(options, values, texts);
	for(var i = 0; i < options.length; i++) {
		if(i == 0) {
			$(options[i]).attr('selected', 'selected');
		} else {
			$(options[i]).removeAttr('selected');
		}
	}
}

$(window).load(function () {
	curr_min_bedroom = 0;
	curr_max_bedroom = 99999999999;
	curr_sale_type = 'R';

	reset_sales_options("rentals");

	// Adding bedrooms to the minimum bedroom selector
	var options = $('select#min_bedrooms-select option');
	var values = [0].concat(bedrooms.slice(0,bedrooms.length - 1));
	var texts = [min_text].concat(bedrooms.slice(0,bedrooms.length - 1));
	show_hide_options(options, values, texts);
	
	// Adding bedrooms to the maximum bedroom selector
	options = $('select#max_bedrooms-select option');
	values = [99999999999].concat(bedrooms.slice(1,bedrooms.length));
	values[values.length - 1] = 99999999999;
	texts = [max_text].concat(bedrooms.slice(1,bedrooms.length));
	texts[texts.length - 1] = texts[texts.length - 1] + '+';
	show_hide_options(options, values, texts);
});

/* Populating the selectors END */

/* Handling the changes in min/max selects and sale type START */

function handle_select_change (changed, other, type) {
	$(changed).change(function () {
		var sel = $(changed + ' option:selected');
		var options = $(other + ' option');
		var m = type == 'min' ? 1 : -1;

		for(var i = 0; i < options.length; i++) {
			if($(options[i]).attr('value') != -1 && m * $(sel).attr('value') < m * $(options[i]).attr('value')) {
				$(options[i]).show();
			} else {
				$(options[i]).hide();
			}
		}
	});
}


$(window).load(function () {
	// Handling sale type.
	$("input[name='sale_type']").change(function() {
		if($("input[name='sale_type']:checked").val() == 'S') {
			console.log('S');
			curr_sale_type = 'S'
			reset_sales_options("sales");
		} else {
			console.log('R');
			curr_sale_type = 'R';
			reset_sales_options("rentals");
		}
	});

	// Handling min price change
	handle_select_change('#min_price-select', '#max_price-select', 'min');

	// Handling max price change
	handle_select_change('#max_price-select', '#min_price-select', 'max');

	// Handling min bedroom change
	handle_select_change('#min_bedrooms-select', '#max_bedrooms-select', 'min');

	// Handling max bedroom change
	handle_select_change('#max_bedrooms-select', '#min_bedrooms-select', 'max');
});

/* Handling the changes in min/max selects and sale type END */

/* Handling search by map START */

$(window).load(function () {
	$(document).keyup(function (e) {
		if(e.keyCode == 27) {
			$('div#map_modal').fadeOut();
		}
	});

	$('div#map_modal .close').click(function () {
		$('div#map_modal').fadeOut();
	});

	$('a#search_by_map_link').click(function (event) {
		event.preventDefault();
		console.log('Clicked on search map link');

		$('div#map_modal').fadeIn();
		if(all_property_ids.length != 0) {
			if(search_map_not_ready) {
				search_map_not_ready = false;

				var latlng = new google.maps.LatLng(51.50015240, -0.12623620);
				var options = {
					zoom: 11,
					center: latlng,
					mapTypeId: google.maps.MapTypeId.HYBRID,
					mapTypeControl: false
				};
				var search_map = new google.maps.Map($('div#map_box').get(0), options);
				
				for(pid in all_property_ids) {
					latlng = all_property_coords[all_property_ids[pid]];
					marker = new google.maps.Marker({position: latlng, map: search_map, title: 'No title', icon: 'https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=home|ffffff|000000'});
					marker.content = prop_contents[all_property_ids[pid]];
					marker.prop_id = all_property_ids[pid];
					google.maps.event.addListener(marker, 'click', function () {
						console.log('Got a click on ', marker.prop_id);
						var ib = new InfoBubble({
							map: this.map,
							content: this.content,
							shadowStyle: 1,
							padding: 0,
							backgroundColor: 'rgb(255,255,255)',
							borderRadius: 0,
							borderWidth: 1,
							disableAutoPan: true,
          					hideCloseButton: true,
						});
						ib.open(marker.map, this);
					});
				}
			}
		}
	});
});

/* Handling search by map END */

/* Functions related to the map's infowindow START */

function info_detail (prop_num) {
	var form = document.createElement("form");
	form.setAttribute("method", "POST");
	form.setAttribute("action", "/" + curr_lang_code + "/detail/" + prop_num + "/");

	var csrf = document.createElement('input');
	csrf.setAttribute("type", "hidden");
	csrf.setAttribute("name", "csrfmiddlewaretoken");
	csrf.setAttribute("value", csrf_token);	
	form.appendChild(csrf);
	
	form.submit();
}

function info_shortlist (prop_num) {
	// Adding new element to the array
	if($.inArray(prop_num, shortlist_ids) == -1) {
		shortlist_ids.push(prop_num);
	}

	// Refreshing the shortlist count
	$('.shortlist-link').each( function () {
		if(this.tagName == 'DIV') {
			$(this).find('a').text($(this).find('a').text().replace(/(.*)\([0-9]+\) >$/, '$1(' + shortlist_ids.length + ') >'));
		}
		else {
			$(this).text($(this).text().replace(/(.*)\([0-9]+\) >$/, '$1(' + shortlist_ids.length + ') >'));
		}
	});

	// Refreshing the cookie related to the shortlist
	$.cookie('shortlist_ids', '[' + shortlist_ids.join(', ') + ']', {'expires': 10000});
}

/* Functions related to the map's infowindow END */

/* Handling the email alert button START */

function email_alert () {
	
}

/* Handling the email alert button END */