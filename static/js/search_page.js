/* Handling pagination, ordering and page change events. */

// This function is handling the rendering of the page numbers
handle_page_numbers = function(curr_page, last_page, res_count) {
	// Calculating the slice of page numbers which will be displayed.
	var slice = [];

	if(last_page - curr_page < 2) {
		var need_after = 2 - (last_page - curr_page);

		for(var i = Math.max(1,curr_page - 2 - need_after); i <= Math.min(curr_page + 2, last_page); i++) {
			slice.push(i);
		}
	} else {
		var need_before;
		if(curr_page - 1 < 2) {
			need_before = 2 - (curr_page - 1);
		} else {
			need_before = 0;
		}

		for(var i = Math.max(1, curr_page - 2); i <= Math.min(curr_page + 2 + need_before, last_page); i++) {
			slice.push(i);
		}
	}

	// Creating the new page links and removing the old ones
	$('li.page_number').each(function () {
		if(slice.indexOf(parseInt($(this).text())) != -1) {
			if(parseInt($(this).find('a').text()) == curr_page) {
				$(this).addClass('selected');
			} else if($(this).hasClass('selected')) {
				$(this).removeClass('selected');
			}
			$(this).show()
		} else {
			if($(this).hasClass('selected')) {
				$(this).removeClass('selected');
			}
			$(this).hide();
		}
	});
}

// Shows or hides the next/prev link based on which page are we on.
handle_next_prev = function (curr,max) {
	if(curr == 1) {
		$('li.prev').css('visibility', 'hidden');
	} else {
		$('li.prev').css('visibility', 'visible');
	}

	if(curr == max) {
		$('li.next').css('visibility', 'hidden');
	} else {
		$('li.next').css('visibility', 'visible');
	}
};

// Loads the search results based on which page are we on and how many results need to be shown on a given page.
handle_item_changes = function(curr_page, next_page, res_per_page, res_count) {
	results = $('div#search_results div.result');

	if(curr_page != next_page) {
		for(var i = (curr_page - 1) * res_per_page; i < Math.min(curr_page * res_per_page, res_count); i++) {
			$(results[i]).hide();
		}

		for(var i = (next_page - 1) * res_per_page; i < Math.min(next_page * res_per_page, res_count); i++) {
			$(results[i]).show();
		}		
	}
};



$(window).load(function () {
	var current_page = 1;
	var curr_total_pages;
	var result_count = $('div#search_results div.result').length;

	if(result_count % curr_result_per_page == 0) {
		curr_total_pages = result_count / curr_result_per_page;
	} else {
		curr_total_pages = Math.floor(result_count / curr_result_per_page) + 1;
	}

	handle_next_prev(current_page, curr_total_pages);

	// Adding the initial page numbers
	handle_page_numbers(current_page, curr_total_pages, result_count);

	// Adding the initial search results to the page.
	var to = Math.min(result_count, curr_result_per_page);
	var results = $('div#search_results div.result');
	for(var i = 0; i < result_count; i++) {
		if(i >= to) {
			$(results[i]).hide();
		}
	}

	// Handling a page change via next button
	$('li.next a').each(function () {
		$(this).click( function (event) {
			event.preventDefault();
			current_page = current_page + 1;
			
			// Changing the available page numbers
			handle_page_numbers(current_page, curr_total_pages, result_count);

			// Hiding next and/or prev if necessary
			handle_next_prev(current_page, curr_total_pages);

			// Changing the items currently displayed
			handle_item_changes(current_page - 1, current_page, curr_result_per_page, result_count);
		});
	});

	// Handling a page change via the prev button
	$('li.prev a').each(function () {
		$(this).click( function (event) {
			event.preventDefault();
			current_page = current_page - 1;
			
			// Changing the available page numbers
			handle_page_numbers(current_page, curr_total_pages, result_count);

			// Hiding next and/or prev if necessary
			handle_next_prev(current_page, curr_total_pages);

			// Changing the items currently displayed
			handle_item_changes(current_page + 1, current_page, curr_result_per_page, result_count);
		});
	});	

	// Handling a page change via clicking on a page number
	$('li.page_number a').each(function () {
		$(this).click(function (event) {
			event.preventDefault();
			var new_page = parseInt($(this).text());
			
			// Changing the available page numbers
			handle_page_numbers(new_page, curr_total_pages, result_count);

			// Hiding next and/or prev if necessary
			handle_next_prev(new_page, curr_total_pages);

			// Changing the items currently displayed
			handle_item_changes(current_page, new_page, curr_result_per_page, result_count);

			current_page = new_page;
		});
	});

	// Handling change of result per page
	$('select[name="per_page"]').change(function () {
		curr_result_per_page = parseInt($(this).find('option:selected').attr('value'));

		// Setting the other selector to the same value
		$('select[name="per_page"] option').each(function () {
			if(parseInt($(this).attr('value')) == curr_result_per_page) {
				$(this).attr('selected', "selected");
			} else {
				$(this).removeAttr('selected');
			}
		});
		
		if(result_count % curr_result_per_page == 0) {
			curr_total_pages = result_count / curr_result_per_page;
		} else {
			curr_total_pages = Math.floor(result_count / curr_result_per_page) + 1;
		}

		var next_page = 1;
		
		// Changing the available page numbers
		handle_page_numbers(next_page, curr_total_pages, result_count);

		// Hiding next and/or prev if necessary
		handle_next_prev(next_page, curr_total_pages);

		// Changing the items currently displayed
		var t = Math.min(result_count, curr_result_per_page);
		var r = $('div#search_results div.result');
		for(var i = 0; i < result_count; i++) {
			if(i >= t) {
				$(r[i]).hide();
			} else {
				$(r[i]).show();
			}
		}

		current_page = next_page;
	});

	// Handling change of ordering
	$('select[name="sort_by"]').change(function () {
		curr_ordering = $('select[name="sort_by"] option:selected').attr('value');

		var ord_r = $('div#search_results div.result').get();

		ord_r.sort(function (a,b) {
			var aPriceText = $(a).find('span.price').attr('id');
			var pricePattern = /[0-9]+_price_([0-9]+)/g;
			var match = pricePattern.exec(aPriceText);
			var aPrice = parseInt(match[1]);

			var bPriceText = $(b).find('span.price').attr('id');
			pricePattern = /[0-9]+_price_([0-9]+)/g;
			match = pricePattern.exec(bPriceText);
			var bPrice = parseInt(match[1]);
			
			if(curr_ordering == 'plh') {
				return (aPrice < bPrice) ? -1 : (aPrice > bPrice) ? 1 : 0;				
			} else { // curr_ordering == 'phl'
				return (aPrice > bPrice) ? -1 : (aPrice < bPrice) ? 1 : 0;
			}	
		});

		var holder = $('div#search_results');
		$.each(ord_r, function (index, item) { holder.append(item); });
	});

	// TODO: Handling the page change based on what's on the map.

});

/* Handling the main area:
 - Image sliders.
 - Shortlist buttons.
 - View details buttons.
 */

$(window).load(function () {
	
	// This handles the changing of the images.
	$('div.controls ul li').each(function () {
		$(this).click(function () {
			var reg = /([^_]+)_([^_]+)/g;
			var match = reg.exec($(this).find('a').text());
			var id = match[1];
			var num = match[2];

			reg = /([^_]+)_([^_]+)/g;
			match = reg.exec($('div#result_' + id + ' div.result_image div.controls ul li.selected a').text());

			var old_num = match[2];
			
			// Adding the old picture to it's holder
			$('#' + id + '_' + old_num + '_holder').append($('#result_' + id + ' img:first'));

			// Adding the new picture from it's holder
			$('div#result_' + id + ' div.result_image').prepend($('#' + id + '_' + num + '_holder' + ' img'));			

			// Deselecting the old carousel
			$('#' + id + '_' + old_num + '_car').removeClass('selected');

			// Selecting the new carousel
			$('#' + id + '_' + num + '_car').addClass('selected');
		});
	});

	// Handling of the shortlist button.
	$('a.button_1').each(function () {
		$(this).click( function (event) {
			event.preventDefault();
			var reg = /shortlist_button_([0-9]+)/g;
			var match = reg.exec($(this).attr('id'));
			var id = match[1];
			
			// Adding new element to the array
			if($.inArray(id, shortlist_ids) == -1) {
				shortlist_ids.push(id);
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
		});
	});

	// Handling of the view details button
	$('a.button_2').each(function () {
		$(this).click(function (event) {
			event.preventDefault();
			var detail_pattern = /result_button_([0-9]+)$/g;
			var detail_match = detail_pattern.exec(this.id);
			var detail_id = detail_match[1];

			var form = document.createElement("form");
			form.setAttribute("method", "POST");
			form.setAttribute("action", "/" + curr_lang_code + "/detail/" + detail_id + "/");

			var hidden = document.createElement('input');
			hidden.setAttribute("type", "hidden");
			hidden.setAttribute("name", "property_ids");
			hidden.setAttribute("value", '[ ' + found_property_ids.join(', ') + ' ]');
			form.appendChild(hidden);

			var csrf = document.createElement('input');
			csrf.setAttribute("type", "hidden");
			csrf.setAttribute("name", "csrfmiddlewaretoken");
			csrf.setAttribute("value", csrf_token);	
			form.appendChild(csrf);
			
			form.submit();
		});
	});
});


/* We set up the map here for viewing the results. */
$(window).load(function () {
	// When clicking on View results by map "button" this function gets called.
	$('div.search_by_map a').each( function () {
		$(this).click(function (event) {
			event.preventDefault();

			$('div#map_modal').fadeIn();
			
			$('body').keyup(function (e) {
				if(e.keyCode == 27) {
					$('body').unbind('keyup');
					$('div#map_modal').fadeOut();
				}
			});

			bounds = new google.maps.LatLngBounds();

			if(found_property_ids.length != 0) {
				if(search_map_not_ready) {
					console.log('creating new map');
					search_map_not_ready = false;
					map_type = "found";

					var latlng = new google.maps.LatLng(51.50015240, -0.12623620);
					var options = {
						zoom: 11,
						center: latlng,
						mapTypeId: google.maps.MapTypeId.HYBRID,
						mapTypeControl: false
					};
					map = new google.maps.Map($('div#map_box').get(0), options);
					
					for(i in found_property_ids ) {
						latlng = found_property_coords[found_property_ids[i]];
						bounds.extend(latlng)
						marker = new google.maps.Marker({position: latlng, map: map, title: 'No title', icon: 'https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=home|ffffff|000000'});
						found_markers.push(marker);
						google.maps.event.addListener(marker, 'click', function () {
							console.log('got clicked')
							// TODO: This should be replaced with a customized infowindow
						});
					}

					// Blowing up the map so we get a "margin" around the properties
					ne = bounds.getNorthEast();
					sw = bounds.getSouthWest();
					bounds.extend(new google.maps.LatLng(ne.lat() + 0.05, ne.lng() + 0.05 ));
					bounds.extend(new google.maps.LatLng(sw.lat() - 0.05, sw.lng() - 0.05));

					map.panToBounds(bounds);
				} else {
					if(map_type != "found") {
						for( i in all_markers) {
							all_markers[i].setMap(null);
						}

						if( found_markers.length == 0 ) {
							for( i in found_property_ids ) {
								latlng = found_property_coords[found_property_ids[i]];
								bounds.extend(latlng);
								marker = new google.maps.Marker({position: latlng, map: map, title: 'No title', icon: 'https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=home|ffffff|000000'});
							}
						} else {
							for( i in found_markers ) {
								found_markers[i].setMap(map)
								bounds.extend(found_markers[i].getPosition());
							}	
						}
						
						// Blowing up the map so we get a "margin" around the properties
						ne = bounds.getNorthEast();
						sw = bounds.getSouthWest();
						bounds.extend(new google.maps.LatLng(ne.lat() + 0.05, ne.lng() + 0.05 ));
						bounds.extend(new google.maps.LatLng(sw.lat() - 0.05, sw.lng() - 0.05));

						map.panToBounds(bounds);
					}
				}
			}
		});
	});
});