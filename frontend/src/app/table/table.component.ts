import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';

@Component({
	selector: 'app-table',
	templateUrl: './table.component.html',
	styleUrls: ['./table.component.css']
})
export class TableComponent {
	rows: any[] = [];

	dataSource = new MatTableDataSource(this.rows);

	constructor(private http: HttpClient) { }

	ngOnInit() {
		let url = `http://0.0.0.0:5000/passwords`;

		const headers = new HttpHeaders().set('Content-Type', 'application/json');
		const options = { headers, withCredentials: true };

		this.http.get<any>(url, options).subscribe(
			response => {
				this.rows = response;
			},
		);
	}
}