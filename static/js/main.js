$("#randSearch").click(function () {
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Main/Random_SearchFilm/',
        success: function(data) {
            outputFilmInfo("outputFilm", data)
            // alert('ok');
            },
        error: function (data) {
            alert('Error');
        }
    })
});
$("#categorySearch").click(function () {
    var genre1=$('#genre1 option:selected').text();
    var startYear=$('#startYear option:selected').text();
    var endYear=$('#endYear option:selected').text();
    var country=$('#country option:selected').text();
    var rating='';
    if($('#star-4:checked').val()=='true')
    {
        rating=5;
    }
    else
    {
        if($('#star-3:checked').val()=='true')
        {
            rating=4;
        }
        else
        {
            if($('#star-2:checked').val()=='true')
            {
                rating=3;
            }
            else
            {
                if($('#star-1:checked').val()=='true')
                {
                    rating=2;
                }
                else
                {
                    if($('#star-0:checked').val()=='true')
                    {
                        rating=1;
                    }
                    else
                    {
                        rating=0;
                    }
                }
            }
        }
    }
    // var genre1=document.getElementById('genre1');
    // var startYear=document.getElementById('startYear');
    // var endYear=document.getElementById('endYear');
    // var coutnry=document.getElementById('country');
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Main/Category_SearchFilm/',
        data: {
            genre1: genre1,
            startYear: startYear,
            endYear:endYear,
            country:country,
            rating:rating
        },
        success: function(data) {
            outputFilmInfo("outputFilm", data)
            // alert('ok');
            },
        error: function (data) {
            alert('Error');
        }
    })
});
$("#randSearchProfile").click(function () {
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Profile/Profile_Random_SearchFilm/',
        success: function(data) {
            outputFilmInfoProfile("outputFilm", data)
            // alert('ok');
            },
        error: function (data) {
            alert('Error');
        }
    })
});
$("#categorySearchProfile").click(function () {
    var genre1=$('#genre1 option:selected').text();
    var startYear=$('#startYear option:selected').text();
    var endYear=$('#endYear option:selected').text();
    var country=$('#country option:selected').text();
    var rating='';
    if($('#star-4:checked').val()=='true')
    {
        rating=5;
    }
    else
    {
        if($('#star-3:checked').val()=='true')
        {
            rating=4;
        }
        else
        {
            if($('#star-2:checked').val()=='true')
            {
                rating=3;
            }
            else
            {
                if($('#star-1:checked').val()=='true')
                {
                    rating=2;
                }
                else
                {
                    if($('#star-0:checked').val()=='true')
                    {
                        rating=1;
                    }
                    else
                    {
                        rating=0;
                    }
                }
            }
        }
    }
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Profile/Profile_Category_SearchFilm/',
        data: {
            genre1: genre1,
            startYear: startYear,
            endYear:endYear,
            country:country,
            rating:rating
        },
        success: function(data) {
            outputFilmInfoProfile("outputFilm", data)
            // alert('ok');
            },
        error: function (data) {
            alert('Error');
        }
    })
});
function outputFilmInfo(id, data) {
    var obj = document.getElementById(id);
    $('#outputFilm').css('display','inline-block');
    $('#filmName').text(data.data[0]);
    $('#filmImage').attr('src',data.data[1]);
    $('#filmOriginal').text(data.data[2]);

    $('.film-genre').remove();

    var elemGenre=data.data[3];
    var g=document.getElementById('filmGenres');
    for(var i=0;i<elemGenre.length;i++)
    {
        let elementA = document.createElement('label');
        elementA.setAttribute('class', 'film-genre');
        elementA.textContent=elemGenre[i]
        g.insertAdjacentHTML('beforeend',elementA.outerHTML);
    }
    $('#filmYear').text("Год: "+data.data[4]);
    var elemCoyntry=data.data[5];
    var countryStr='';
    for(var i=0;i<elemCoyntry.length-1;i++)
    {
        countryStr+=elemCoyntry[i]+', ';
    }
    countryStr+=elemCoyntry[elemCoyntry.length-1]
    $('#filmCountry').text(countryStr);
    $('#filmDuration').text(data.data[6]);
    $('#filmProducer').text("Режиссер: "+data.data[7]);
    //
    $('.str').remove();

    var rating=Math.round(data.data[8]);
    var notrating=5-rating;
    var r=document.getElementById('filmRating');
    while(rating>0)
    {
        let elementspan = document.createElement('span');
        elementspan.setAttribute('class', 'str');
        elementspan.style.fontSize='1.25rem';
        elementspan.style.color='rgb(255,187,0)';

        let elementi = document.createElement('i');
        elementi.setAttribute('class', 'fas fa-star');

        elementspan.insertAdjacentHTML('beforeend',elementi.outerHTML);
        r.insertAdjacentHTML('beforeend',elementspan.outerHTML);
        rating=rating-1;
    }
    while(notrating>0)
    {
        let elementspan = document.createElement('span');
        elementspan.setAttribute('class', 'str');
        elementspan.style.fontSize='1.25rem';
        elementspan.style.color='rgb(177,176,172)';

        let elementi = document.createElement('i');
        elementi.setAttribute('class', 'fas fa-star');

        elementspan.insertAdjacentHTML('beforeend',elementi.outerHTML);
        r.insertAdjacentHTML('beforeend',elementspan.outerHTML);
        notrating=notrating-1;
    }
    $('#filmText').text(data.data[9]);
    $('#filmLikes').text(data.data[10]+' likes');
}
function outputFilmInfoProfile(id, data) {
    var obj = document.getElementById(id);
    $('#outputFilm').css('display','inline-block');
    $('#filmName').text(data.data[0]);
    $('#filmImage').attr('src',data.data[1]);
    $('#filmOriginal').text(data.data[2]);

    $('.film-genre').remove();

    var elemGenre=data.data[3];
    var g=document.getElementById('filmGenres');
    for(var i=0;i<elemGenre.length;i++)
    {
        let elementA = document.createElement('label');
        elementA.setAttribute('class', 'film-genre');
        elementA.textContent=elemGenre[i]
        g.insertAdjacentHTML('beforeend',elementA.outerHTML);
    }
    $('#filmYear').text("Год: "+data.data[4]);
    var elemCoyntry=data.data[5];
    var countryStr='';
    for(var i=0;i<elemCoyntry.length-1;i++)
    {
        countryStr+=elemCoyntry[i]+', ';
    }
    countryStr+=elemCoyntry[elemCoyntry.length-1]
    $('#filmCountry').text(countryStr);
    $('#filmDuration').text(data.data[6]);
    $('#filmProducer').text("Режиссер: "+data.data[7]);
    //
    $('.str').remove();

    var rating=Math.round(data.data[8]);
    var notrating=5-rating;
    var r=document.getElementById('filmRating');
    while(rating>0)
    {
        let elementspan = document.createElement('span');
        elementspan.setAttribute('class', 'str');
        elementspan.style.fontSize='1.25rem';
        elementspan.style.color='rgb(255,187,0)';

        let elementi = document.createElement('i');
        elementi.setAttribute('class', 'fas fa-star');

        elementspan.insertAdjacentHTML('beforeend',elementi.outerHTML);
        r.insertAdjacentHTML('beforeend',elementspan.outerHTML);
        rating=rating-1;
    }
    while(notrating>0)
    {
        let elementspan = document.createElement('span');
        elementspan.setAttribute('class', 'str');
        elementspan.style.fontSize='1.25rem';
        elementspan.style.color='rgb(177,176,172)';

        let elementi = document.createElement('i');
        elementi.setAttribute('class', 'fas fa-star');

        elementspan.insertAdjacentHTML('beforeend',elementi.outerHTML);
        r.insertAdjacentHTML('beforeend',elementspan.outerHTML);
        notrating=notrating-1;
    }
    $('#filmText').text(data.data[9]);
    $('#filmLikes').text(data.data[10]+' likes');
    var t=data.data[11]
    if(data.data[11]==true){
        var like=document.getElementById('likeIcon');

        like.classList.remove("far");
        like.classList.add("fas");
    }
    else
    {
        var like=document.getElementById('likeIcon');

        like.classList.remove("fas");
        like.classList.add("far");
    }
    $('.comment-card').remove();
    var elemComment=data.data[12];
    var out=document.getElementById('outputFilm');
    for(var i=0;i<elemComment.length;i++)
    {
        let elementdiv = document.createElement('div');
        elementdiv.setAttribute('class', 'col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 comment-card');
        elementdiv.style.display='inline-block';

        let elementh = document.createElement('h4');
        elementh.style.display='inline-block';
        elementh.style.marginRight='2rem';
        elementh.textContent=elemComment[i][0]

        let elementl1 = document.createElement('label');
        elementl1.setAttribute('class', 'small');
        elementl1.textContent=elemComment[i][1]

        let elementl2 = document.createElement('label');
        elementl2.setAttribute('class', 'film-coment');
        elementl2.style.width='100%';
        elementl2.textContent=elemComment[i][2]

        let elementhr=document.createElement('hr');

        elementdiv.insertAdjacentHTML('beforeend',elementh.outerHTML);
        elementdiv.insertAdjacentHTML('beforeend',elementl1.outerHTML);
        elementdiv.insertAdjacentHTML('beforeend',elementl2.outerHTML);
        elementdiv.insertAdjacentHTML('beforeend',elementhr.outerHTML);
        out.insertAdjacentHTML('beforeend',elementdiv.outerHTML);
    }
    var c=data.data[13]
    if(data.data[13]==true){
        var clock=document.getElementById('clockIcon');

        clock.classList.remove("far");
        clock.classList.add("fas");
    }
    else
    {
        var clock=document.getElementById('clockIcon');

        clock.classList.remove("fas");
        clock.classList.add("far");
    }
    var s=data.data[14]
    if(data.data[14]==true){
        var star=document.getElementById('starIcon');

        star.classList.remove("far");
        star.classList.add("fas");
    }
    else
    {
        var star=document.getElementById('starIcon');

        star.classList.remove("fas");
        star.classList.add("far");
    }
}
function outputFilmComment(data)
{
    $('.comment-card').remove();
    var elemComment=data.data;
    var out=document.getElementById('outputFilm');
    for(var i=0;i<elemComment.length;i++)
    {
        let elementdiv = document.createElement('div');
        elementdiv.setAttribute('class', 'col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 comment-card');
        elementdiv.style.display='inline-block';

        let elementh = document.createElement('h4');
        elementh.style.display='inline-block';
        elementh.style.marginRight='2rem';
        elementh.textContent=elemComment[i][0]

        let elementl1 = document.createElement('label');
        elementl1.setAttribute('class', 'small');
        elementl1.textContent=elemComment[i][1]

        let elementl2 = document.createElement('label');
        elementl2.setAttribute('class', 'film-coment');
        elementl2.style.width='100%';
        elementl2.textContent=elemComment[i][2]

        let elementhr=document.createElement('hr');

        elementdiv.insertAdjacentHTML('beforeend',elementh.outerHTML);
        elementdiv.insertAdjacentHTML('beforeend',elementl1.outerHTML);
        elementdiv.insertAdjacentHTML('beforeend',elementl2.outerHTML);
        elementdiv.insertAdjacentHTML('beforeend',elementhr.outerHTML);
        out.insertAdjacentHTML('beforeend',elementdiv.outerHTML);
    }
}
$('#likeIcon').click(function () {
    var filmName=document.getElementById('filmName').textContent
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Profile/AddLike/',
        data: {
            filmName:filmName
        },
        success: function(data) {
            $('#filmLikes').text(data.data[0]+' likes');
            if(data.data[1]==true)
            {
                var like=document.getElementById('likeIcon');

                like.classList.remove("far");
                like.classList.add("fas");
            }
            else
            {
                var like=document.getElementById('likeIcon');

                like.classList.remove("fas");
                like.classList.add("far");
            }
        },
        error: function (data) {
            alert('Error');
        }
    })
})
$('#sendComment').click(function () {
    var filmName=document.getElementById('filmName').textContent
    var commentText=document.getElementById('comText').value
    $('#closeComment').click();
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Profile/AddComment/',
        data: {
            filmName:filmName,
            commentText:commentText
        },
        success: function(data) {
            // alert('ok');
            outputFilmComment(data);
        },
        error: function (data) {
            alert('Error');
        }
    })
})
$('#clockIcon').click(function () {
    var filmName=document.getElementById('filmName').textContent
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Profile/AddWantSee/',
        data: {
            filmName:filmName
        },
        success: function(data) {
            var t=data.data[0]
            if(data.data[0]==true)
            {
                var clock=document.getElementById('clockIcon');

                clock.classList.remove("far");
                clock.classList.add("fas");
            }
            else
            {
                var clock=document.getElementById('clockIcon');

                clock.classList.remove("fas");
                clock.classList.add("far");
            }
        },
        error: function (data) {
            alert('Error');
        }
    })
})
$('#starIcon').click(function () {
    var filmName=document.getElementById('filmName').textContent
    $.ajax({
        type:"GET",
        dataType:"json",
        url:'/Profile/AddFavorite/',
        data: {
            filmName:filmName
        },
        success: function(data) {
            var t=data.data[0]
            if(data.data[0]==true)
            {
                var star=document.getElementById('starIcon');

                star.classList.remove("far");
                star.classList.add("fas");
            }
            else
            {
                var star=document.getElementById('starIcon');

                star.classList.remove("fas");
                star.classList.add("far");
            }
        },
        error: function (data) {
            alert('Error');
        }
    })
})

$('#send').click(function () {
    $('#alert').css('display','none');
    var name=document.getElementById('inputName').value
    var email=document.getElementById('inputEmail').value
    var pass1=document.getElementById('inputPassword1').value
    var pass2=document.getElementById('inputPassword2').value
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var error='';
    if(name=='' || email=='' || pass1=='' || pass2=='')
    {
        error='Заполнены не все поля!';
        $('#alert').css('display','block');
        $('#alert').text(error);
    }
    else
    {
        if(reg.test(email) == false)
        {
            // alert('Введите корректный e-mail');
            // return false;
            error='Введите корректный e-mail!';
            $('#alert').css('display','block');
            $('#alert').text(error);
        }
        else
        {
            if(pass1!=pass2)
            {
                error='Пароли не совпадают!';
                $('#alert').css('display','block');
                $('#alert').text(error);
            }
            else
            {
                $.ajax({
                type:"GET",
                dataType:"json",
                url:'/Main/Registrate/',
                data: {
                    name: name,
                    email: email,
                    pass1:pass1
                },
                success: function(data) {
                    // alert('ok');
                    $('#suc').css('display','block');
                    $('.form-group').css('display','none');
                    $('#send').css('display','none');
                    $('#cancel').css('display','none');
                    // outputFilmInfo("outputFilm", data)
                    },
                error: function (data) {
                    alert('Error');
                    }
                })
            }
        }
    }

})


$('#sendAuth').click(function () {
    $('#alert').css('display','none');
    var email=document.getElementById('inputEmail').value
    var pass=document.getElementById('inputPassword').value
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var error='';
    if(email=='' || pass=='')
    {
        error='Заполнены не все поля!';
        $('#alert').css('display','block');
        $('#alert').text(error);
    }
    else
    {
        if(reg.test(email) == false)
        {
            // alert('Введите корректный e-mail');
            // return false;
            error='Введите корректный e-mail!';
            $('#alert').css('display','block');
            $('#alert').text(error);
        }
        else
        {
                $.ajax({
                type:"GET",
                dataType:"json",
                url:'/Main/Authorize/',
                data: {
                    email: email,
                    passw:pass
                },
                success: function(data) {
                    if(data.data=='true') {
                        window.location.href = '/Profile';
                    }
                    else
                    {
                        alert('Error');
                        error='Не верная пара логин пароль!';
                        $('#alert').css('display','block');
                        $('#alert').text(error);
                    }
                    },
                error: function (data) {
                    alert('Error');
                    error='Не верная пара логин пароль!';
                    $('#alert').css('display','block');
                    $('#alert').text(error);
                    }
                })
        }
    }

})