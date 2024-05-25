# VideoDrome Project Test File

## Table of contents

## Manual Testing

Manual testing was done for each completed user story and screenshots added to the comments on each issue page.

|User Story|Results|Detail|
|----------|-------|-------------|


## Compatibility and Responsive Testing


### Windows laptop

This project was developed using a Windows laptop running Windows 10 and the site was viewed on three browsers.

|Browser|Dimensions|Screen|
|-------|----------|------|
|Chrome|1920x1080||
|Firefox|1920x1080||
|Edge|1920x1080||


### Chrome Emulated Device Dimensions

|Device Name|Dimensions|Screen|
|-----------|----------|------|

### Browserstack Devices

[Browserstack.com](https://www.browserstack.com/)

|Device|OS|Browser|Viewport|Screen|
|------|--|-------|--------|------|

### Market Share insights

I used [statcounter.com](https://gs.statcounter.com/) to give me an idea of which devices, browsers and operating systems I should focus on due to their popularity.

|Data|Image|
|----|-----||

## Accessibility Testing


### Accessibility Audits

#### Performance, Accessibility, Best Practices and SEO

[PageSpeed Insights](https://pagespeed.web.dev/) was used to audit the site's features for performance, accessibility, best practices and SEO. This was recommended as a more accurate reading than Chrome's lighthouse tool. The site scored 100 throughout on accessibly, best practice and SEO, which is good. Performance wise, the site runs much better on desktop than it does mobile. For a better performance on mobile, time could be taken to look in to optimising Cumulative Layout Shift, First Contentful Paint and largest Contentful Paint.

|Page|Factor|Performance|Accessibility|Best Practices|SEO|Screen Capture|
|----|------|-----------|-------------|--------------|---|--------------|

[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) Was used to check for errors and contrast errors throughout the site.

|Page|Result|Screen Capture|
|----|------|--------------|

### Keyboard Navigation

Using a reference from [https://webaim.org](https://webaim.org/techniques/keyboard/#testing) I tested the keyboard navigation options that were relevant to the site (side scrolling or radio inputs couldn't be tested for example as they're not utilised on the site).

- [ ] Tab key navigates forward to interactive elements.
- [ ] Shift+Tab navigates backward to interactive elements.
- [ ] Enter key activates links.
- [ ] Enter or Spacebar activate buttons.
- [ ] ↑/↓ - navigate between dropdown menu options.
- [ ] Spacebar expands dropdown menu options.
- [ ] Enter/Esc select dropdown menu option and collapse.
- [ ] Typing letters jumps to a dropdown menu option.
- [ ] Esc button closes modal dialogue box.
- [ ] ↑/↓ buttons scroll vertically
- [ ] Spacebar/Shift + Spacebar scroll by page (no button in focus).

## Validation Testing

### CSS Validation

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code through direct input.

|Result|Screen Capture|
|------|--------------|

### HTML Validation

[W3C  Markup Validation Service](https://validator.w3.org/) was used to validate the html through direct code input. The html was acquired for each page by viewing the page source code on the deployed site.

|Page|Result|Screen Capture|
|----|------|--------------|



### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the javascript files through direct input of code.

`/*jshint esversion: 6 */` Was added to the test to remove ES6 warnings.

`import * as bootstrap from 'bootstrap';` Was also added to the test to remove an udefinded variable error (if included in app code this line breaks modal function).

|File|Result|Screen Capture|
|----|------|--------------|

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the relevant python files through direct input of code.

|File|Result|Screen Capture|
|----|------|--------------|

## Automated Testing

As time was short, the automated testing done on this project was small and very basic. The Code Institute walkthought project 'I Think, Therfore I Blog" informed the initial tests while the TestHomePage unit test was inspired by django documentation on automated tests [(here)](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#example).


## Defects


## Defects of Note


## Outstanding Defects

No known defects outstanding.
