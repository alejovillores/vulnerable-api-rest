import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
	selector: 'app-search',
	templateUrl: './search.component.html',
	styleUrls: ['./search.component.css']
})
export class SearchComponent {
	rows: any[] = [];
	text: string = '';

	constructor(private http: HttpClient) { }

	searchPasswords() {
		let url = `http://0.0.0.0:5000/password?app_name=${this.text}`;

		const headers = new HttpHeaders().set('Content-Type', 'application/json');
		const options = { headers, withCredentials: true };

		this.http.get<any>(url, options).subscribe(
			response => {
				console.log(response);
				this.rows = response;
			},
		);
	}
}