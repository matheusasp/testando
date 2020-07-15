var request = new XMLHttpRequest();

request.open('POST', 'https://api.huggy.io/v2/flows/81773/contact/14777306/exec');

request.setRequestHeader('Content-Type', 'application/json');
request.setRequestHeader('Authorization', 'Bearer 61c408a6be2981c7e2070a3beb09ef97');
request.setRequestHeader('Accept', 'application/json');

request.onreadystatechange = function () {
  if (this.readyState === 4) {
    console.log('Status:', this.status);
    console.log('Headers:', this.getAllResponseHeaders());
    console.log('Body:', this.responseText);
  }
};

var body = {
  'uuid': '2fa8b297-076b-4234-b0d8-2f1aa864d857',
  'variables': {
    'data': '15/10/2019',
    'url_evento': 'https://huggy.io'
  },
  'whenInChat': true,
  'whenWaitForChat': true,
  'whenInAuto': true
};

request.send(JSON.stringify(body));