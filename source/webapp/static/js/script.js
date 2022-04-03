function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function onLoad() {
    let quoteList = document.getElementById("quote-list")
    let url = "api/v1/quote/"
    let response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        }
    )
    let answer = await response.json()
    for (quote of answer) {
        if (quote.name) {
            if (quote.email) {
                quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a> <div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><p>Автор Цитаты: " + quote.name + "</p><p>Адрес Почты: " + quote.email + "</p> </div><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
            } else {
                quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a> <div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><p>Автор Цитаты: " + quote.name + "</p></div><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
            }
        } else {
            if (quote.email) {
                quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a> <div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><p>Адрес Почты: " + quote.email + "</p> </div><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
            } else {
                quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a></div><div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
            }

        }

    }


}

async function onQuoteClick(event) {
    let quoteList = document.getElementById("quote-list")
    while (quoteList.firstChild) {
        quoteList.removeChild(quoteList.firstChild);
    }
    let pk = event.target.dataset.pk
    let url = "api/v1/quote/" + pk
    let response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        }
    )
    let quote = await response.json()
    if (quote.name) {
        if (quote.email) {
            quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a> <div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><p>Автор Цитаты: " + quote.name + "</p><p>Адрес Почты: " + quote.email + "</p> </div><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
        } else {
            quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a> <div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><p>Автор Цитаты: " + quote.name + "</p></div><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
        }
    } else {
        if (quote.email) {
            quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a> <div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><p>Адрес Почты: " + quote.email + "</p> </div><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
        } else {
            quoteList.innerHTML += "<div class='quote-one'><a data-pk='" + quote.id + "' onclick='onQuoteClick(event)' class='quote'>" + quote.text + "</a></div><div class='quote-information'><p id='" + quote.id + "'><span data-pk='" + quote.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + quote.rating + "    <span data-pk='" + quote.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span></p><div class='quote-date'><p>Дата создание: " + quote.created_at + "</p></div></div>"
        }

    }
}

async function modalCreateOpen() {
    let quoteList = document.getElementById("quote-list")
    while (quoteList.firstChild) {
        quoteList.removeChild(quoteList.firstChild);
    }
    let modal = document.getElementById('myModal');
    modal.style.display = "block"
}

async function modalCreateClose() {
    let modal = document.getElementById('myModal');
    modal.style.display = "none"
    onLoad()
}

async function createQuote() {
    let text = document.getElementById("text").value
    let name = document.getElementById("name").value
    let email = document.getElementById("email").value
    let csrftokens = getCookie('csrftoken');
    let url = "api/v1/quote/create/"
    let data = {"text": text, "name": name, "email": email}
    let response = await fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokens
        }
    })
    if (response.status === "500") {
        alert("Произошла ошибка!")
    } else {
        alert("Цитата успешно создана!")
    }
}

async function ratingUp(event) {
    let pk = event.target.dataset.pk
    let url = "api/v1/quote/" + pk + "/rating/add/"
    let csrftokens = getCookie('csrftoken');
    let info = document.getElementById(pk)
    let response = await fetch(url, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokens
        }
    })
    let answer = await response.json()
    info.innerHTML = "<span data-pk='" + answer.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + answer.rating + "    <span data-pk='" + answer.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span>"
}

async function ratingDown(event) {
    let pk = event.target.dataset.pk
    let url = "api/v1/quote/" + pk + "/rating/remove/"
    let csrftokens = getCookie('csrftoken');
    let info = document.getElementById(pk)
    let response = await fetch(url, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokens
        }
    })
    let answer = await response.json()
    info.innerHTML = "<span data-pk='" + answer.id + "' onclick='ratingUp(event)' class='rating up'>⇑</span>    " + answer.rating + "    <span data-pk='" + answer.id + "' onclick='ratingDown(event)' class='rating down'>⇓</span>"
}


window.onload = onLoad