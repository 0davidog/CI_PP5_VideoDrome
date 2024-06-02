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
|index|mobile|
|index|desktop|

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
|No Error Found.|[W3C CSS Result Screenshot.](https://github.com/0davidog/VideoDrome/assets/135815736/c0f33359-54b0-4bc0-aae2-e5754c8f3b12)|


### HTML Validation

[W3C  Markup Validation Service](https://validator.w3.org/) was used to validate the html through direct code input. The html was acquired for each page by viewing the page source code on the deployed site. The checkout page could not be included in this test due to stripes security features causing the source to be blocked from view.

|Page|Result|Screen Capture|
|----|------|--------------|
|index|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/2381b825-3913-4b05-8807-4663eff9f12c)|
|videos|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/c250df64-7f46-4e3c-883f-84c45b7ab692)|
|customer|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/196e68b1-ea72-4b82-84ae-9248b8c9a93c)|
|customer/update_info|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/5c3e00f8-2ba9-4c1b-9aba-b1f13d2aa651)|
|customer/view_wishlist|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/c0c278a1-9a56-4404-95bf-8ea4de06698c)|
|customer/saved_address|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d3d67292-5f61-4280-96bc-c5066f360f1f)|
|customer/read_reviews|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/78f1078d-c5d1-42d2-a83e-cdc2b8404448)|
|customer/create_messages|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/449cb639-c8a4-4a1f-9d49-cb11e89bd8a7)|
|customer/read_messages|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/a79e9971-0384-4e89-8b57-03e4c8945648)|
|customer/inventory|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/5deeb811-75d8-4081-862b-123fab51fc95)|
|customer/orders|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/c9f95b0d-9b55-4899-b3e4-d663d46d8e94)|
|customer/order_detail|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/8c975789-1e63-4857-a0d3-863595f55615)|
|basket|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/6e753647-b696-4f83-8deb-a49e8738bcb3)|
|checkout/checkout_success/|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/fb5f9c68-b7b5-400e-bcf0-af21f10e8f7c)

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the javascript files through direct input of code.

`/*jshint esversion: 6 */` Was added to the test to remove ES6 warnings.

`import * as bootstrap from 'bootstrap';` Was also added to the test to remove an udefinded variable error (if included in app code this line breaks modal function).

|File|Result|Screen Capture|
|----|------|--------------|
|background.js|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/7e39d8a3-be22-4ce3-bdb8-ec72b8f1b305)|
|basket.js|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/82699b6e-520b-4f6a-8fd3-9868f87e49ab)|
|stars.js|Two Warnings|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/27dddabe-eda1-4d07-be1b-b7dbdebb6c8c)|
|stripe.js|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/da285747-58c8-48e2-b745-fc0b8ea8e610)|
|toast.js|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/efa89a99-3452-4797-bca4-7ef3760d37a5)|

The warning 'Functions declared within loops referencing an outer scoped variable may lead to confusing semantics' was ignored on stars.js as it didn't seem a serious issue for the time being.

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the relevant python files through direct input of code.

#### Videodrome App

|File|Result|Screen Capture|
|----|------|--------------|
|urls.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/498671f8-480c-4eb1-800e-b8dc4bd8d6bf)|

#### Video App

|File|Result|Screen Capture|
|----|------|--------------|
|views.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/cea8b3de-fa9d-462d-8a07-2b8f9de853f6)|
|urls.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/92f389c4-8039-4c9d-bf6f-169ac3087519)|
|models.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/72219b46-0691-4fc3-b40d-b50cd3bed226)|
|forms.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/89bd7770-9d2a-4a3a-b689-e72d83573ada)|
|contexts.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/83f2f0c8-7ec0-46cc-b95a-8c99136fc9ce)|
|admin.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d8957608-fc10-408c-964e-fdb59d6da13c)|

#### Main App

|File|Result|Screen Capture|
|----|------|--------------|
|views.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/5a474108-0946-4900-aacc-d8913994f6f8)|
|urls.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/8ac10cc1-75bc-4957-a003-fbfab664ff22)|

#### Customer App

|File|Result|Screen Capture|
|----|------|--------------|
|views.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d739c177-482a-426b-acc3-e8064f2de473)|
|urls.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/c9a87ea5-aeb5-47d3-b159-44519e0642c9)|
|models.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/aa38d79f-586c-40e9-aa15-c8aad7be66ed)|
|forms.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/3807df02-cf67-4bad-8694-bd1dc2e8d21f)|
|email.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/0b5bc12e-2b0a-4e6f-80f5-f3b1f17e4863)|
|admin.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/898aff10-9967-4829-8d72-60f7930fe1c1)|

#### Checkout App

|File|Result|Screen Capture|
|----|------|--------------|
|webhooks.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/3379f6ee-0f7e-4e26-8f3e-e0fe0daefd4c)|
|webhook_handler.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/afa6cdcc-1c2a-4bba-bdd3-3fc6c410e020)|
|views.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/68c34f6a-b1ed-43b4-951f-f0cd1ab789c9)|
|urls.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/57248f47-2abb-4693-a196-e0a65a988549)|
|signals.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/438c7916-6e6e-4250-aed6-2d324445f2c2)|
|models.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/567fb410-fa7a-4a1c-bfb5-db41f2aabf67)|
|forms.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/97230568-d4e4-4a14-a547-04480c7f6e35)|
|email.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/0f3fd9a2-3914-48de-9297-1f21dc018eb3)|
|admin.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/e9c82721-6506-4de4-b283-011c98d7d0f8)|

#### Basket App

|File|Result|Screen Capture|
|----|------|--------------|
|views.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/da41bd2d-8469-420b-a777-23028de98c90)|
|urls.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/bb46067a-0ac2-4a6f-aa8a-cc66e89871fe)|
|contexts.py|Good|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/4b6e0c4b-cee0-499c-950b-77cd0709faa8)|

## Automated Testing

As time was short, the automated testing done on this project was small and very basic. The Code Institute walkthought project 'I Think, Therfore I Blog" informed the initial tests while the TestHomePage unit test was inspired by django documentation on automated tests [(here)](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#example).


## Defects


## Defects of Note


## Outstanding Defects

No known defects outstanding.
