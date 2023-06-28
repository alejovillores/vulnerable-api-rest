import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
	selector: 'app-generic-popup',
	templateUrl: './generic-popup.component.html',
	styleUrls: ['./generic-popup.component.css']
})
export class GenericPopupComponent {
	title: string;
	message: string;

	constructor(@Inject(MAT_DIALOG_DATA) public data: any) {
		this.title = data.title;
		this.message = data.message;
	}
}