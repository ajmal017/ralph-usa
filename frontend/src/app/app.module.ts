import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { BotComponent } from './components/bot/bot.component';
import { HttpClientModule } from '@angular/common/http';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToolbarComponent } from './components/toolbar/toolbar.component';
import { AboutComponent } from './components/about/about.component';
import { MatChipsModule, MatDialogModule, MatFormFieldModule, MatIconModule, MatOptionModule, MatSelectModule, MatSliderModule, MatToolbarModule } from '@angular/material';
import { AssetModalComponent } from './components/asset-modal/asset-modal.component';
import { PerformancePaneComponent } from './components/performance-pane/performance-pane.component';
import { DashboardGraphsComponent } from './components/dashboard-graphs/dashboard-graphs.component'



@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    BotComponent,
    ToolbarComponent,
    AboutComponent,
    AssetModalComponent,
    PerformancePaneComponent,
    DashboardGraphsComponent
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatIconModule,
    MatToolbarModule, 
    MatChipsModule,
    MatDialogModule,
    MatFormFieldModule,
    MatOptionModule,
    MatSelectModule,
    MatSliderModule, 
    NgxChartsModule
  ],
  entryComponents: [
    AssetModalComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }