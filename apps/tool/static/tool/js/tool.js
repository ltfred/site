//get url params
var getParam = function(name){
    var search = document.location.search;
    var pattern = new RegExp("[?&]"+name+"\=([^&]+)", "g");
    var matcher = pattern.exec(search);
    var items = null;
    if(null != matcher){
            try{
                    items = decodeURIComponent(decodeURIComponent(matcher[1]));
            }catch(e){
                    try{
                            items = decodeURIComponent(matcher[1]);
                    }catch(e){
                            items = matcher[1];
                    }
            }
    }
    return items;
};

//baidu links push api
function push_spider(CSRF, URL) {
	var url = $.trim($('#form-url').val());
	var urls = $.trim($('#form-urls').val());
	if (url.length == 0 | urls.length == 0) {
		alert('接口地址和网址链接内容都不能为空！');
		return false
	};
	$.ajaxSetup({
		data: {
			csrfmiddlewaretoken: CSRF
		}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'url': url,
			'url_list': urls
		},
		dataType: 'json',
		success: function(ret) {
			$('.push-result').html(ret.msg);
		},
	})
}

//sitemap urls baidu push api
function site_push_spider(CSRF, URL) {
	var url = $.trim($('#form-url').val());
	var map_url = $.trim($('#form-sitemap').val());
	if (url.length == 0 | map_url.length == 0) {
		alert('接口地址和sitemap地址内容都不能为空！');
		return false
	};
	$.ajaxSetup({
		data: {
			csrfmiddlewaretoken: CSRF
		}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'url': url,
			'map_url': map_url
		},
		dataType: 'json',
		success: function(ret) {
			$('.push-result').html(ret.msg);
		},
	})
}

//regex api
function regex_api(CSRF, URL) {
	var r = $.trim($('#form-regex').val());
	var texts = $.trim($('#form-text').val());
	if (r.length == 0 | texts.length == 0) {
		alert('待提取信息和正则表达式都不能为空！');
		return false
	};
	$.ajaxSetup({
		data: {
			csrfmiddlewaretoken: CSRF
		}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'r': r,
			'texts': texts,
			'key':getParam('key')
		},
		dataType: 'json',
		success: function(ret) {
		    var newhtml = '<div class="text-left re-result">' + ret.result + "</div>"
			$('.push-result').html(newhtml);
		},
	})
}

// picture to base64
function picture_to_base64_api(CSRF, URL){
	if ($("#picture").val() === '') {
		alert('请先选择图片！');
		return false
	};
	let formData = new FormData();
	formData.append('picture', document.getElementById('picture').files[0]);
	formData.append("csrfmiddlewaretoken", CSRF)
	formData.append("is_header", $("input[name='optradio']:checked").val())
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
	url:URL,
	type:"post",
	data: formData,
	contentType: false,
	processData: false,
	success: function(ret) {
		var newhtml = '<textarea class="form-control rounded-0" id="form-result" rows="8">' + ret.result + "</textarea>"
		$('.push-result').html(newhtml);
	},
	error: function (ret) {
		var newhtml = '<div class="text-left re-result">' + "似乎出了点问题呢" + "</div>"
		$('.push-result').html(newhtml);
	}
})

}

//user-agent api
function useragent_api(CSRF, URL) {
    var d_tags = $("#device_type input:checkbox:checked");
    var os_tags = $("#os input:checkbox:checked");
    var n_tags = $("#navigator input:checkbox:checked");
    var d_lis = new Array();
    var os_lis = new Array();
    var n_lis = new Array();
    if (d_tags.length > 0){
        for (var i=0;i<d_tags.length;i++){
            d_lis.push(d_tags[i].value);
        }
    };
    if (os_tags.length > 0){
        for (var i=0;i<os_tags.length;i++){
            os_lis.push(os_tags[i].value);
        }
    };
    if (n_tags.length > 0){
        for (var i=0;i<n_tags.length;i++){
            n_lis.push(n_tags[i].value);
        }
    };
	$.ajaxSetup({
		data: {
			csrfmiddlewaretoken: CSRF
		}
	});
	$.ajax({
		type: 'post',
		url: URL,
		data: {
		    'd_lis': d_lis.join(),
			'os_lis': os_lis.join(),
			'n_lis': n_lis.join()
		},
		dataType: 'json',
		success: function(ret) {
			$('.push-result').text(ret.result)
		},
	})
}

//docker search
function docker_search(CSRF, URL) {
	var name = $.trim($('#image-name').val());
	if (name.length == 0) {
		alert('待查询的镜像名称不能为空！');
		return false
	};
	$.ajaxSetup({
		data: {
			csrfmiddlewaretoken: CSRF
		}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'name': name,
		},
		dataType: 'json',
		success: function(ret) {
		    var newhtml = '<table class="table table-bordered my-0"><thead class="thead-light"><tr><th scope="col">镜像版本</th>' +
		        '<th scope="col">镜像大小</th><th scope="col">更新时间</th></tr></thead><tbody>';
            for (var i=0;i < ret.results.length; i++) {
				var item = ret.results[i]
                newhtml += '<tr><th scope="row">' + item.name + '</th><td>' + item.full_size + '</td><td>' + item.last_updated + '</td></tr>'
            }
		    newhtml += '</tbody></table>'
			$('.push-result').html(newhtml);
		},
		error: function(XMLHttpRequest) {
			var _code = XMLHttpRequest.status;
			if (_code == 404) {
				var error_text = '镜像仓库没有查询到相关信息，请检查镜像名称后重试！';
			} else if (_code == 500) {
				var error_text = '请求超时，请稍后重试！'
			} else {
				var error_text = '未知错误...'
			}
			var newhtml = '<div class="my-2">' + error_text + '</div>';
			$('.push-result').html(newhtml);
		}
	})
}


// base64加解密
function base64_api(CSRF, URL, FLAG) {
	var texts = $.trim($('#form-text').val());
	if (texts.length === 0) {
	alert('请输入要加密或解密的内容！');
	return false
	}
	$.ajaxSetup({
	data: {
		csrfmiddlewaretoken: CSRF
	}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'texts': texts,
			"flag": FLAG,
		},
		dataType: 'json',
		success: function(ret) {
			if (ret.status === 400) {
				var newhtml = '<div class="text-left re-result">' + ret.result + "</div>"
				$('.push-result').html(newhtml);
			} else if (ret.status === 200) {
				var newhtml = '<textarea class="form-control rounded-0" id="form-result" rows="8">' + ret.result + "</textarea>"
				$('.push-result').html(newhtml);
			}
		},
	})

}


//phone api
function phone_api(CSRF, URL) {
	var phone = $.trim($('#form-phone').val());
	if (phone.length === 0) {
		alert('手机号不能为空！');
		return false
	}
	if(!(/^1[3456789]\d{9}$/.test(phone))){
	alert("手机号码有误，请重填");
	return false
	}
	$.ajaxSetup({
		data: {
			csrfmiddlewaretoken: CSRF
		}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'phone': phone,
		},
		dataType: 'json',
		success: function(ret) {
			if (ret.code === 200) {
				var newhtml = '<div class="text-left re-result">' + '省份：' + ret.result["province"] + '<br>' + '城市：' + ret.result["city"] + '<br>' + '运营商：' + ret.result["company"] + '<br>' + '区号：' + ret.result["areacode"] + '<br>'+ "</div>"
				$('.push-result').html(newhtml);
			} else {
				var newhtml = '<div class="text-left re-result">' + ret.msg + "</div>"
				$('.push-result').html(newhtml);
			}

		},
	})
}


function rgb_api(CSRF, URL) {
	var rgb = $.trim($('#form-rgb').val());
	if (rgb.length === 0) {
		alert('输入的不能为空！');
		return false
	}
	$.ajaxSetup({
	data: {
		csrfmiddlewaretoken: CSRF
	}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'rgb': rgb,
		},
		dataType: 'json',
		success: function(ret) {
			if (ret.code === 0) {
				var newhtml = '<div class="text-left re-result">' + ret.extra + '<div>' + ret.result + '</div>' + "</div>"
				$('.push-result').html(newhtml);
			} else {
				var newhtml = '<div class="text-left re-result">' + ret.msg + "</div>"
				$('.push-result').html(newhtml);
			}

		},
	})
}


function bmi_api(CSRF, URL) {
	var height = $.trim($('#form-height').val());
	var weight = $.trim($('#form-weight').val());
	if (height.length === 0 | weight.length === 0) {
		alert('输入的不能为空！');
		return false
	}
	$.ajaxSetup({
	data: {
		csrfmiddlewaretoken: CSRF
	}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'height': height,
			'weight': weight,
		},
		dataType: 'json',
		success: function(ret) {
			if (ret.code === 200) {
				var newhtml = '<div class="text-left re-result">' + ret.message + "</div>"
				$('.push-result').html(newhtml);
				console.log(ret.message)
			} else {
				var newhtml = '<div class="text-left re-result">' + ret.message + "</div>"
				$('.push-result').html(newhtml);
			}

		},
	})
}


function link_api(CSRF, URL) {
	var name = $.trim($('#form-name').val());
	var address = $.trim($('#form-address').val());
	var desc = $.trim($('#form-desc').val());
	var logo = $.trim($('#form-logo').val());
	var email = $.trim($('#form-email').val());
	if (name.length === 0) {
		alert('输入的网站名称不能为空！');
		return false
	}
	if (address.length === 0) {
		alert('输入的网站链接不能为空！');
		return false
	}
	if (desc.length === 0) {
		alert('输入的网站简介不能为空！');
		return false
	}
	$.ajaxSetup({
	data: {
		csrfmiddlewaretoken: CSRF
	}
	});
	$('.push-result').html('<i class="fa fa-spinner fa-pulse fa-3x my-3"></i>');
	$.ajax({
		type: 'post',
		url: URL,
		data: {
			'name': name,
			'address': address,
			'desc': desc,
			'logo': (logo || ""),
			'email': (email || ""),
		},
		dataType: 'json',
		success: function(ret) {
			if (ret.code === 200) {
				var newhtml = '<div class="text-left re-result">' + ret.message + "</div>"
				$('.push-result').html(newhtml);
				console.log(ret.message)
			} else {
				var newhtml = '<div class="text-left re-result">' + ret.message + "</div>"
				$('.push-result').html(newhtml);
			}

		},
	})
}
