/* Script for handling the images START */

var curr_image = 1;
var small_offset;
var big_offset;

function image_changer (dir) {
	if(dir == 'prev') {
		curr_image -= 1;
		if(curr_image == 1) {
			$('a#prev_big_image').hide();
		}
		$('a#next_big_image').show();
		$('div#big_inner_holder').animate({'left': '+=698'}, 'slow');
		small_offset = document.getElementById('small_image_' + (curr_image + 1)).clientWidth;
		$('div#small_inner_holder').animate({'left': '+=' + small_offset}, 'slow');
	} else { // dir == 'next'
		curr_image += 1;
		if(curr_image == total_images) {
			$('a#next_big_image').hide();
		}
		$('a#prev_big_image').show();
		$('div#big_inner_holder').animate({'left': '-=698'}, 'slow');
		small_offset = document.getElementById('small_image_' + curr_image).clientWidth;
		$('div#small_inner_holder').animate({'left': '-=' + small_offset}, 'slow');
	}
}

$(window).load(function () {
	$('a#prev_big_image').hide();
	if(total_images == 1) {
		$('a#next_big_image').hide();
	}

	// Handling prev button clicks
	$('a#prev_big_image').click(function (event) {
		event.preventDefault();
		image_changer('prev');
	});

	// Handling next button clicks
	$('a#next_big_image').click(function (event) {
		event.preventDefault()
		image_changer('next');
	});

	// Handling direct thumb image clicks.
	$('img.small_image').each(function () {
		$(this).click(function () {
			var prev_small_image = curr_image + 1;
			var pattern = /small_image_([0-9]+)/g;
			var next_small_image = parseInt(pattern.exec($(this).attr('id'))[1]);

			if(next_small_image != 1 && next_small_image != total_images + 2) {
				curr_image = next_small_image - 1;
				small_offset = 0;

				if(curr_image == total_images) {
					$('a#next_big_image').hide();
					if(total_images == 1) {
						$('a#prev_big_image').hide();
					} else {
						$('a#prev_big_image').show();
					}
				} else if(curr_image == 1) {
					$('a#prev_big_image').hide();
					if(total_images == 1) {
						$('a#next_big_image').hide();
					} else {
						$('a#next_big_image').show();
					}
				} else {
					$('a#prev_big_image').show();
					$('a#next_big_image').show();
				}

				if(prev_small_image < next_small_image) {
					for(var i = prev_small_image; i < next_small_image; i++) {
						small_offset += document.getElementById('small_image_' + i).clientWidth;
					}
					big_offset = (next_small_image - prev_small_image) * 698;
					$('div#small_inner_holder').animate({'left': '-=' + small_offset}, 'slow');
					$('div#big_inner_holder').animate({'left': '-=' + big_offset}, 'slow');
				} else if(prev_small_image > next_small_image) {
					for(var i = prev_small_image; i > next_small_image; i--) {
						small_offset += document.getElementById('small_image_' + i).clientWidth;	
					}
					big_offset = (prev_small_image - next_small_image) * 698;
					$('div#small_inner_holder').animate({'left': '+=' + small_offset}, 'slow');
					$('div#big_inner_holder').animate({'left': '+=' + big_offset}, 'slow');
				}
			}
		});
	});
});

/* Script for handling the images END */

/* Handlers for links above the main area START */

$(window).load( function () {
	$('a#detail-image_link').click(function (event) {
		event.preventDefault();
		$('div#map_holder').hide();
		$('div#floorplan_holder').hide();
		$('div#feature').show();
		$('a#detail-map_link').parent().removeClass('selected');
		$('a#detail-floorplan_link').parent().removeClass('selected');
		$('a#detail-image_link').parent().addClass('selected');
	});

	var map_not_loaded = true;

	$('a#detail-map_link').click(function (event) {
		event.preventDefault();
		if (map_not_loaded) {
			map_not_loaded = false;
			map_loader();
		};
		$('div#map_holder').show();
		$('div#floorplan_holder').hide();
		$('div#feature').hide();
		$('a#detail-map_link').parent().addClass('selected');
		$('a#detail-floorplan_link').parent().removeClass('selected');
		$('a#detail-image_link').parent().removeClass('selected');
	});

	$('a#detail-floorplan_link').click(function (event) {
		event.preventDefault();
		$('div#map_holder').hide();
		$('div#floorplan_holder').show();
		$('div#feature').hide();
		$('a#detail-map_link').parent().removeClass('selected');
		$('a#detail-floorplan_link').parent().addClass('selected');
		$('a#detail-image_link').parent().removeClass('selected');
	});	
});


/* Handlers for links above the main area END */

/* Setting up the page at page load  START */

function submitter (url, hidden_name, hidden_value) {
	var form = document.createElement("form");
	form.setAttribute("method", "POST");
	form.setAttribute("action", url);

	var hidden = document.createElement('input');
	hidden.setAttribute("type", "hidden");
	hidden.setAttribute("name", hidden_name);
	hidden.setAttribute("value", hidden_value);
	form.appendChild(hidden);

	var csrf = document.createElement('input');
	csrf.setAttribute("type", "hidden");
	csrf.setAttribute("name", "csrfmiddlewaretoken");
	csrf.setAttribute("value", csrf_token);	
	form.appendChild(csrf);
	
	form.submit();
}

$(window).load(function () {
	$('div#map_holder').hide();
	$('div#floorplan_holder').hide();

	if(property_ids.length == 0) {
		$('div.result_bar a.prev').css('visibility', 'hidden');
		$('div.result_bar a.next').css('visibility', 'hidden');
		$('div.result_bar a.back').css('visibility', 'hidden');
	} else {
		if(property_ids.indexOf(curr_property_id) == 0) {
			$('div.result_bar a.prev').css('visibility', 'hidden');
		} else {
			$('div.result_bar a.prev').click(function () {
				submitter('/' + curr_lang_code + '/detail/' + property_ids[property_ids.indexOf(curr_property_id) - 1] + '/', 'property_ids', "[" + property_ids.join(', ') + "]");	
			});
		}

		if(property_ids.indexOf(curr_property_id) == property_ids.length - 1) {
			$('div.result_bar a.next').css('visibility', 'hidden');
		} else {
			$('div.result_bar a.next').click(function () {
				submitter('/' + curr_lang_code + '/detail/' + property_ids[property_ids.indexOf(curr_property_id) + 1] + '/', 'property_ids', "[" + property_ids.join(', ') + "]");
			});
		}

		$('a.back').click(function () {
			submitter("/" + curr_lang_code + "/search/", "shortlist_ids", "[" + property_ids.join(', ') + "]");	
		});
	}
});

/* Setting up the page at page load  END */

/* The function that populates the map. START */

function map_loader() {
	var latlng = new google.maps.LatLng(curr_property_coord[0], curr_property_coord[1]);
	var options = {
		zoom: 14,
		center: latlng,
		mapTypeId: google.maps.MapTypeId.HYBRID,
		mapTypeControl: false
	};
	var map = new google.maps.Map($('div#map_holder').get(0), options);

	if(property_ids.length != 0) {
		for(var i = 0; i < property_ids.length; i++) {
			if(property_ids[i] != curr_property_id) {
				latlng = new google.maps.LatLng(property_coords[2 * i], property_coords[2 * i + 1]);
				marker = new google.maps.Marker({position: latlng, map: map, title: 'No title', icon: 'https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=home|ffffff|000000'});
				marker.property_id = property_ids[i];
				
				// We need to add the new listener to this page.
				google.maps.event.addListener(marker, 'click', function () {
					var form = document.createElement("form");
					form.setAttribute("method", "POST");
					form.setAttribute("action", "/" + curr_lang_code + "/detail/" + this.property_id + "/");

					var hidden = document.createElement('input');
					hidden.setAttribute("type", "hidden");
					hidden.setAttribute("name", "property_ids");
					hidden.setAttribute("value", "[" + property_ids.join(', ') + "]");
					form.appendChild(hidden);

					var csrf = document.createElement('input');
					csrf.setAttribute("type", "hidden");
					csrf.setAttribute("name", "csrfmiddlewaretoken");
					csrf.setAttribute("value", csrf_token);	
					form.appendChild(csrf);
					
					form.submit();
				});
			}
		}
	}

	latlng = new google.maps.LatLng(curr_property_coord[0], curr_property_coord[1]);
	marker = new google.maps.Marker({position: latlng, map: map, title: 'No title', icon: 'https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=home|f89829|000000'});
};

/* The function that populates the map. END */

/* Code to handle adding the current property to the shortlist START */

$(window).load(function () {
	$('a#detail-shortlist_link').click( function (event) {
			event.preventDefault();
			
			// Adding new element to the array if needed
			if($.inArray(curr_property_id, shortlist_ids) == -1) {
				shortlist_ids.push(curr_property_id);

				
				// Refreshing the shortlist count
				$('.shortlist-link').each( function () {
					if(this.tagName == 'DIV') {
						$(this).find('a').text($(this).find('a').text().replace(/(.*)\([0-9]+\) >$/, '$1(' + shortlist_ids.length + ') >'));
					} else {
						$(this).text($(this).text().replace(/(.*)\([0-9]+\) >$/, '$1(' + shortlist_ids.length + ') >'));
					}
				});

				// Refreshing the cookie related to the shortlist
				$.cookie('shortlist_ids', '[' + shortlist_ids.join(', ') + ']', {'expires': 10000});
			}
		});
});

/* Code to handle adding the current property to the shortlist END */