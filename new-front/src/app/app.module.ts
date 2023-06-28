import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTabsModule } from '@angular/material/tabs';
import { MatTableModule } from '@angular/material/table';
import { FormComponent } from './form/form.component';
import { TableComponent } from './table/table.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { LoginComponent } from './login/login.component';
import { HttpClientModule } from '@angular/common/http';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { SearchComponent } from './search/search.component';
import { MatButtonModule } from '@angular/material/button';
import { NavbarComponent } from './navbar/navbar.component';
import { SuccessPopupComponent } from './success-popup/success-popup.component';
import { GenericPopupComponent } from './generic-popup/generic-popup.component';
import { LoginServiceComponent } from './login-service/login-service.component';

@NgModule({
  declarations: [
    AppComponent,
    FormComponent,
    GenericPopupComponent,
    LoginServiceComponent,
    LoginComponent,
    NavbarComponent,
    SearchComponent,
    SuccessPopupComponent,
    TableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTabsModule,
    MatTableModule,
    FormsModule,
    ReactiveFormsModule,
    MatDialogModule,
    HttpClientModule,
    MatSnackBarModule,
    MatButtonModule
  ],
  providers: [{ provide: MAT_DIALOG_DATA, useValue: {} }, { provide: MatDialogRef, useValue: {} }, LoginServiceComponent],
  bootstrap: [AppComponent]
})
export class AppModule { }
