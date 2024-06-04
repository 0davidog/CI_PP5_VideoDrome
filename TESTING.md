# VideoDrome Project Test File

## Table of contents

- [VideoDrome Project Test File](#videodrome-project-test-file)
  - [Manual Testing](#manual-testing)
  - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    - [Windows laptop](#windows-laptop)
    - [Chrome Emulated Device Dimensions](#chrome-emulated-device-dimensions)
    - [Browserstack Devices](#browserstack-devices)
    - [Market Share insights](#market-share-insights)
  - [Accessibility Testing](#accessibility-testing)
    - [Accessibility Audits](#accessibility-audits)
      - [Performance, Accessibility, Best Practices and SEO](#performance-accessibility-best-practices-and-seo)
    - [Keyboard Navigation](#keyboard-navigation)
  - [Validation Testing](#validation-testing)
    - [CSS Validation](#css-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
  - [Automated Testing](#automated-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
  - [Outstanding Defects](#outstanding-defects)

## Manual Testing

Manual testing was done for each completed user story and screenshots added to the comments on each issue page.

|User Story|
|----------|
|[As a new user, I want to be able to register an account on the website using my email address and password.](https://github.com/0davidog/VideoDrome/issues/1)|
|[As a registered user, I want to be able to log in to my account securely so that I can shop easily with my saved information.](https://github.com/0davidog/VideoDrome/issues/2)|
|[As a Site user, I want the option to reset my password in case I forget it, ensuring secure access to my account.](https://github.com/0davidog/VideoDrome/issues/3)|
|[As a Site User, I want a user-friendly navigation menu that helps me explore different sections of the site easily.](https://github.com/0davidog/VideoDrome/issues/32)|
|[As a user, I want to be able to browse products by category so that I can better find the kind of products I'm interested in.](https://github.com/0davidog/VideoDrome/issues/4)|
|[As a user, I want to be able to search for products by name or keyword so that I can find a particular product I'm interested in.](https://github.com/0davidog/VideoDrome/issues/5)|
|[As a user, I want to be able to order products by price or release date, so I can browse in mind of the cheapest or newest items.](https://github.com/0davidog/VideoDrome/issues/14)|
|[As a shopper, I want to view detailed information about a product, including images, descriptions, and specifications so that I can be better informed about my purchases.](https://github.com/0davidog/VideoDrome/issues/6)|
|[As a shopper, I want to be able to read reviews for a product so that I can be better informed before making a purchase decision.](https://github.com/0davidog/VideoDrome/issues/7)|
|[As a registered site-user, I want to be able to add a product to my wishlist so that I can easily return to a product I want to purchase at a more convenient time.](https://github.com/0davidog/VideoDrome/issues/8)|
|[As a registered site-user, I can give a star rating to a product so that I can express my view on product quality without writing a review.](https://github.com/0davidog/VideoDrome/issues/12)|
|[As a shopper, I want to be able to add items to my shopping basket so that I can purchase multiple products in one transaction.](https://github.com/0davidog/VideoDrome/issues/9)|
|[As a shopper, I want to be able to view and edit the contents of my shopping cart before proceeding to checkout so that I can be sure of my final purchase decision.](https://github.com/0davidog/VideoDrome/issues/10)|
|[As a shopper, I want to be able to securely check out and provide shipping and payment information so that I may purchase items with ease and confidence.](https://github.com/0davidog/VideoDrome/issues/15)|
|[As a shopper, I want to be able to view my order history so that I access the information for my records or a query.](https://github.com/0davidog/VideoDrome/issues/25)|
|[As a site-owner, I want to include a site-map to ensure better site navigation and search engine optimisation](https://github.com/0davidog/VideoDrome/issues/17)|
|[As a site owner, I want to Include Meta Description tags in the application HTML so that I can improve search engine optimisation](https://github.com/0davidog/VideoDrome/issues/18)|
|[As a site-owner, I want to include a robots.txt file in my site so that I can control search engine bot crawling, preserve bandwidth and protect sensitive data.](https://github.com/0davidog/VideoDrome/issues/22)|
|[As a site-owner, I want to include a newsletter sign up option, so that I can reach my audience with news and offers in a cost-effective manner.](https://github.com/0davidog/VideoDrome/issues/31)|
|[As a site-owner, I want to include a 404 response page with an appropriate redirect for attempted access to non-existent content so that users who stumble on such errors are not put off from browsing.](https://github.com/0davidog/VideoDrome/issues/23)|
|[As a Site User with accessibility needs, I want the website to be accessible, with features like ALT text for images and keyboard navigation, to ensure a positive experience for all users.](https://github.com/0davidog/VideoDrome/issues/27)|
|[As a site-admin I want to be able to add a product without the admin panel so that my work flow can stay oriented to the site.](https://github.com/0davidog/VideoDrome/issues/28)|
|[As a site-admin I want to be able to edit a product without the admin panel so that my work flow can stay oriented to the site.](https://github.com/0davidog/VideoDrome/issues/29)|
|[As a site-admin I want to be able to edit a product without the admin panel so that my work flow can stay oriented to the site.](https://github.com/0davidog/VideoDrome/issues/30)|

## Compatibility and Responsive Testing

### Windows laptop

This project was developed using a Windows laptop running Windows 10 and the site was viewed on three browsers.

|Browser|Dimensions|Screen|
|-------|----------|------|
|Chrome|1920x1080|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d37f1f41-d9d8-45a6-8abb-bfbc27e47a15)|
|Firefox|1920x1080|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/9910ad32-e58c-4e23-ade3-690d191b2ca9)|
|Edge|1920x1080|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/560b47e2-615b-4229-a36f-6adf4cb34a36)|

### Chrome Emulated Device Dimensions

|Device Name|Dimensions|Screen|
|-----------|----------|------|
|iPhoneSE|375x667|[chrome_screen_01](https://github.com/0davidog/VideoDrome/assets/135815736/a7ef51a5-f9bd-496b-bb0e-b18118203a4a)|
|iPhone XR|414x896|[chrome_screen_02](https://github.com/0davidog/VideoDrome/assets/135815736/351b3cee-f692-4ce9-8eca-a602b7b91d66)|
|iPhone 12 Pro|390x884|[chrome_screen_03](https://github.com/0davidog/VideoDrome/assets/135815736/ebcd01a5-9386-4c3b-9f93-3762e632989b)|
|iPhone 14 Pro Max|430x932|[chrome_screen_04](https://github.com/0davidog/VideoDrome/assets/135815736/6d850d14-4ebc-441d-9bb2-aa817d686882)|
|Pixel 7|412x915|[chrome_screen_05](https://github.com/0davidog/VideoDrome/assets/135815736/76822136-c7dc-49de-a227-1a74dd48f39b)|
|Samsung Galaxy S8+|360x740|[chrome_screen_06](https://github.com/0davidog/VideoDrome/assets/135815736/a2cbed89-5cbf-4f3b-acf7-10a13f01e3d3)|
|Samsung Galaxy S20 Ultra|412x915|[chrome_screen_07](https://github.com/0davidog/VideoDrome/assets/135815736/009b5c8a-e122-491a-a8ce-61a0125d3886)|
|iPad Mini|768x1024|[chrome_screen_08](https://github.com/0davidog/VideoDrome/assets/135815736/e4878edf-fb5e-41c9-b865-bfddbe88c358)|
|iPad Air|820x1180|[chrome_screen_09](https://github.com/0davidog/VideoDrome/assets/135815736/25e47e87-3d6e-4e79-bc8e-062c09565b93)|
|iPad Pro|1024x1366|[chrome_screen_10](https://github.com/0davidog/VideoDrome/assets/135815736/992f4a9a-47b7-48b0-b007-7cf64aac3c2b)|
|Surface Pro 7|912x1368|[chrome_screen_11](https://github.com/0davidog/VideoDrome/assets/135815736/923046e4-d6d5-44fe-8524-825b73653da7)|
|Surface Duo|540x720|[chrome_screen_12](https://github.com/0davidog/VideoDrome/assets/135815736/8eae8328-e9a7-47c7-9ad9-8141079ddf72)|
|Galaxy Z Fold 5|344x882|[chrome_screen_13](https://github.com/0davidog/VideoDrome/assets/135815736/e779ec05-cf4a-4b0e-a825-842d0f1b6fbd)|
|Asus Zenbook Fold|853x1280|[chrome_screen_14](https://github.com/0davidog/VideoDrome/assets/135815736/cddb15a2-17e1-4134-8571-1705cc44302e)|
|Samsung Galaxy A51/71|412x914|[chrome_screen_15](https://github.com/0davidog/VideoDrome/assets/135815736/59139be4-2985-4bc0-9648-e255c7ab7888)|
|Nest Hub|1024x600|[chrome_screen_16](https://github.com/0davidog/VideoDrome/assets/135815736/eb4a8c1b-1655-4eab-9b79-d9fb2b3a62f4)|
|Nest Hub Max|1280x800|[chrome_screen_17](https://github.com/0davidog/VideoDrome/assets/135815736/a6836d41-b6e8-4b68-aef9-b95b62039ee1)|


### Browserstack Devices

[Browserstack.com](https://www.browserstack.com/)

|Device|OS|Browser|Viewport|Screen|
|------|--|-------|--------|------|
|iPhone 14|ios v16.6|Chrome|390x664|[browserstack01](https://github.com/0davidog/VideoDrome/assets/135815736/9f29ba15-aa04-4c35-aad3-c1eb39d719ff)|
|iPhone 15 Pro Max|ios v17.3|Safari|430x932|[browserstack02](https://github.com/0davidog/VideoDrome/assets/135815736/9052de98-52d8-473a-96dc-750af9b3a3a1)|
|Samsung Galaxy S23|Android v13.0|Chromw|393x786|[browserstack03](https://github.com/0davidog/VideoDrome/assets/135815736/e6c2665f-1d61-4bd7-9e8f-16a9ba58ecd7)|
|Xiaomi Redmi Note 12 4G|Android v13.0|Chrome|393x736|[browserstack04](https://github.com/0davidog/VideoDrome/assets/135815736/cc11bcd0-f20b-4302-adb7-f49e0fb749fb)|
|iPad 10th|ios v16.0|Safari|820x1106[browserstack05](https://github.com/0davidog/VideoDrome/assets/135815736/83f093e2-39be-4253-b743-6e08544b2007)|
|Mac|Sonoma|Safari|1920x927|[browserstack06](https://github.com/0davidog/VideoDrome/assets/135815736/0aa54c48-0e9e-492d-b15c-1f9d86dab969)|
|iPhone XS|ios v15.3|Chrome|375x635|[browserstack07](https://github.com/0davidog/VideoDrome/assets/135815736/e4187dbb-8ab3-4ab8-8750-fc26868035f9)|

### Market Share insights

I used [statcounter.com](https://gs.statcounter.com/) to give me an idea of which devices, browsers and operating systems I should focus on due to their popularity.

|Data|Image|
|----|-----|
|Desktop Browser Market Share:|![Screenshot 2024-06-03 at 22-19-36 Desktop Browser Market Share Worldwide Statcounter Global Stats](https://github.com/0davidog/VideoDrome/assets/135815736/7c73cd92-6903-4bf4-b95e-128397082e5c)|
|Mobile Browser Market Share:|![Screenshot 2024-06-03 at 22-20-05 Mobile Browser Market Share Worldwide Statcounter Global Stats](https://github.com/0davidog/VideoDrome/assets/135815736/25152248-98c4-4bd3-8929-4779c5f9bcd6)|
|Mobile Vendor Market Share:|![Screenshot 2024-06-03 at 22-20-44 Mobile Vendor Market Share Worldwide Statcounter Global Stats](https://github.com/0davidog/VideoDrome/assets/135815736/4ea364b5-4542-412c-9935-50265fb0b9d2)|
|Tablet Vendor Market Share:|![Screenshot 2024-06-03 at 22-21-04 Tablet Vendor Market Share Worldwide Statcounter Global Stats](https://github.com/0davidog/VideoDrome/assets/135815736/8e94fc2b-931d-460a-9259-c1b4e6b37182)|
|Operating System Market Share:|![Screenshot 2024-06-03 at 22-21-59 Operating System Market Share Worldwide Statcounter Global Stats](https://github.com/0davidog/VideoDrome/assets/135815736/36ba1e1b-c8aa-46bb-86b5-4514cf251536)|

## Accessibility Testing

### Accessibility Audits

#### Performance, Accessibility, Best Practices and SEO

[PageSpeed Insights](https://pagespeed.web.dev/) was used to audit the site's features for performance, accessibility, best practices and SEO. This was recommended as a more accurate reading than Chrome's lighthouse tool. The site scored 100 throughout on accessibly, best practice and SEO, which is good. Performance wise, the site runs much better on desktop than it does mobile. For a better performance on mobile, time could be taken to look in to optimising Cumulative Layout Shift, First Contentful Paint and largest Contentful Paint.

|Page|Factor|Performance|Accessibility|Best Practices|SEO|Screen Capture|
|----|------|-----------|-------------|--------------|---|--------------|
|index|mobile|70|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/85d613da-9b32-4e39-866d-eafcf788e430)|
|index|desktop|97|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/6b226dde-a3db-4dd1-8037-290463ceaaac)|
|videos|mobile|55|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/e4a222cb-6920-445b-97ed-d1d7c12cc0c4)|
|videos|desktop|90|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/f2a2db3f-d558-4b9a-bd4e-95fc1594ef25)|
|video detail|mobile|64|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/6dd4c1ba-0f92-4e94-88d3-62415c8c50da)|
|video detail|desktop|95|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d8954ccb-c85f-49f7-bb9a-f8958395ad4a)|
|basket|mobile|63|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/dcbd42ca-2ca2-4177-9d9b-d759ab030b1b)|
|basket|desktop|96|100|100|100|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d566cd3a-eba3-4e16-af23-ddba5dcceb30)|

### Keyboard Navigation

Using a reference from [https://webaim.org](https://webaim.org/techniques/keyboard/#testing) I tested the keyboard navigation options that were relevant to the site (side scrolling or radio inputs couldn't be tested for example as they're not utilised on the site).

- [x] Tab key navigates forward to interactive elements.
- [x] Shift+Tab navigates backward to interactive elements.
- [x] Enter key activates links.
- [x] Enter or Spacebar activate buttons.
- [x] ↑/↓ - navigate between dropdown menu options.
- [x] Spacebar expands dropdown menu options.
- [x] Enter/Esc select dropdown menu option and collapse.
- [x] Typing letters jumps to a dropdown menu option.
- [x] Esc button closes modal dialogue box.
- [x] ↑/↓ buttons scroll vertically
- [x] Spacebar/Shift + Spacebar scroll by page (no button in focus).

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
|videos/the-ninth-configuration-blu-ray|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/7281f93b-498f-48b3-9347-8e83fec664e6)|
|customer|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/196e68b1-ea72-4b82-84ae-9248b8c9a93c)|
|customer/update_info|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/5c3e00f8-2ba9-4c1b-9aba-b1f13d2aa651)|
|customer/view_wishlist|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/c0c278a1-9a56-4404-95bf-8ea4de06698c)|
|customer/saved_address|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/d3d67292-5f61-4280-96bc-c5066f360f1f)|
|customer/read_reviews|No errors or warnings to show.|[Screenshot](https://github.com/0davidog/VideoDrome/assets/135815736/78f1078d-c5d1-42d2-a83e-cdc2b8404448)|
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

As time was short, manual testing was focused on for this project. I repeated a test from the Code Institute walkthought project 'I Think, Therfore I Blog" as it was easy to replicate.

videos/test_forms.py Contains one TestCase class: TestReviewForm.

The TestReviewForm class features two methods.

- test_review_form_is_valid() Method: This method tests whether the form is valid when all required fields are properly filled. It creates an instance of ReviewForm with sample data (a title and content), and then checks if the form is valid using assertTrue() assertion. If the form is valid, the test passes; otherwise, it fails.
- test_empty_review_form_is_invalid() Method: This method tests whether the form is invalid when all required fields are empty. It creates another instance of ReviewForm with empty values for all fields and checks if the form is valid using assertFalse() assertion. If the form is invalid (as it should be when all required fields are empty), the test passes; otherwise, it fails.

## Defects

I spent far too long trying to figure out why django and gmail would not cooperate. The entire time I had my own email spelled wrong in env.py.

## Defects of Note

### Webhooks

Due to the complexity of the stripe implementation in this project I attempted to stick close to the 'Boutique Ado' walkthrough project when it came to the checkout app and stripe payments. However, this caused me to end up with a webhook handler that just wasn't working at all. The problem was such that I didn't even know how to look for the cause. The only solution was to go to the stripe documentation an rebuild the webhook from there. The biggest help was downloading the Stripe CLI which allowed me to test the webhook locally and with this installed I was able to see the print statements and error messages and work from there.

## Outstanding Defects

No known defects outstanding.
