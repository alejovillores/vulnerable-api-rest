import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuccessPopupComponent } from './success-popup.component';

describe('SuccessPopupComponent', () => {
  let component: SuccessPopupComponent;
  let fixture: ComponentFixture<SuccessPopupComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SuccessPopupComponent]
    });
    fixture = TestBed.createComponent(SuccessPopupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
