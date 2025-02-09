# SEO User Exchange – Tips Database
The “SEO User Exchange” is an online tool with which owners of small and medium sized businesses can exchange tips and best-practices from their own online marketing efforts in order help each other. All data connected to the tips is stored on an external database that can be accessed and manipulated by users via the frontend. 

## UX
The purpose of the SEO User Exchange is to allow users to exchange tips about what has worked for them in terms of their online marketing. Users can then give each other feedback regarding the usefulness of the tips that are posted via a voting system (up/down). 

The page is for any individual or company worldwide who would like to get tips on good online marketing practices from their peers.  

The SEO User Exchange is the best way to get tips on online marketing from peers because it gives a quick and comprehensive summary of various online marketing tips that have been applied by people in real life. Since it also incorporates a voting system, it also lets users quickly assess the usefulness of each individual tip as perceived by other users. 

- As a user type, I want to get a quick overview of online marketing tips from peers that could work for my business. 
- As a user type, I want to be able to assess and vote on the usefulness of the tips presented. 
- As a user type I want to be able to post, edit and delete online marketing tips that have worked for me. This includes adding, editing and deleting the relevant category of my tip. 

Mockup:






## Features
SEO User Exchange has various features that intend to allow users to get a quick overview of various online marketing tips that have worked for other people and to assess their validity via the social component. It also facilitates the posting, editing and deleting of tips. 

### Existing Features
- List of database entries – All tips are summarized on a list individual cards. Information contained on the cards is tip title, tip description, tip category, number of up/downvotes, date of publishing and edit and delete functionality via links. Results are ordered by number of upvotes in descending order.
- Filtering by category – All results can be filtered by category via a list of clickable links above the results. Filtered results are ordered by number of upvotes in descending order. Filter remains in place upon up or downvote.
- Summary statistics above results – A brief set of summary statistics is displayed above the results indicating the total number of unfiltered/filtered results and the total number new filtered/unfiltered results.
- Pagination – Results are displayed in sets of 5 that can be moved through via pagination links above and below the displayed results.
- Global Data Summary – Database entries are dynamically summarized on a dedicated summary page with graphs.
- User Authentication – Basic login/logout functionality on page enabling database manipulation and voting functionality.
- Adding, editing and deleting tips – Tips can be added, edited and deleted via different links and forms on the page.
- Adding, editing and deleting categories - Categories can be added, edited and deleted via different links and forms on the page.
- Upvoting/Downvoting – Tips can be up- or downvoted via corresponding buttons on page.

All features fully responsive on mobile devices (incl. tablets and smartphones). 

### Features Left to Implement
- 






## Technologies Used
- HTML
    - The project uses HTML code to allow structuring and display of the information presented on MarketingMan.ie.
- Python
- CSS
    - The project uses CSS code to visually design and animate the page's structure as defined by the HTML.
- [Bootstrap](https://getbootstrap.com/docs/3.3/)
    - The project uses the Bootstrap framework (v. 3.3.7) to save time in development by relying on standardized HTML and CSS elements that can be found in the library.
- Materialize
    - o	The project uses the Materialize framework (v. 0.100.2) to save time in development by relying on standardized HTML and CSS elements that can be found in the library.
- [jQuery](https://blog.jquery.com/2017/03/20/jquery-3-2-1-now-available/) & [Bootstrap javascript](https://getbootstrap.com/docs/3.3/getting-started/)
    - The project uses jQuery (v. 3.2.1) and Boostrap javascript (v. 3.2.1) for animation and inclusion of portfolio carousel element.
- D3 & DC
    - The project uses the D3 and DC javascript libraries for the purpose of visualising the SEO data on the site.
- Mlab Database
    - The project uses CSS to visually design the data that is being transmitted via HTML.






## Testing
1.  Quick overview of all posted Online Marketing tips / summary statistics
    1. Go to SEO User Exchange homepage
    2. Verify that summary statistics “total” and “new” display above tip card results and that “total” displays the total number of all results and “new” displays the number of results that were posted on the day of viewing the page.
    3. Verify that tips are ordered in descending order according to number of upvotes and that only 5 results are shown per page and that the remaining results can be accessed via the pagination links.
    4. Try to click on category links above results and verify that depending on selected category, only results for this category are displayed and that the summary statistics above the results change accordingly.
    5. Try to click on “summary” link in top navigation and verify that all 3 graphs (“Tips / Category”, “Upvotes / Tip” and “Tips / Date”) reflect current results and change dynamically when database is edited.

Manual testing revealed that the “tips overview” and “summary pages” were integrated and visualised seamlessly. The pages are accessible on all devices and all major browsers and look virtually the same on different browsers.

2.	Assessing and voting on usefulness of tips
    1. Go to SEO User Exchange homepage
    2. Try scrolling down results and verify that individual tip cards show number of received upvotes (See “Up:”).
    3. OR try to click on “Login” in main navigation and verify that individual tip cards now have an up- and downvote button.
    4. Try to click on either the up- or downvote button and verify that total number of upvotes of the chosen tip goes up or down accordingly.
    5. OR try to click on “login” in main navigation, click on the “Read More” button on an individual tip card (either on filtered or non-filtered results page) and verify that the individual tip card now has an up- and downvote button.
    6. Try to click on either the up- or downvote button and verify that total number of upvotes of the chosen tip goes up or down accordingly.

Manual testing revealed that assessing and voting on tips was integrated and visualised seamlessly. The functionality is accessible on all devices and all major browsers and looks virtually the same on different browsers. 

3.	Posting, editing and deleting tips (incl. tip categories)
    1. Go to SEO User Exchange homepage
    2. Try to click on “login” in top navigation, click “Add Tip!” button on the right of results OR ”New Tip” link in main navigation and verify that form for posting new tip loads correctly and includes fields for “category”, “name, “description” and publishing date.
    3. Try to choose tip category, enter tip name, tip description, select date of publishing, click “ADD TIP” below form and verify that user is redirected to unfiltered results page and that the new tip is included in results.
    4. OR try to click on “login” in main navigation, click on the “Read More” button on an individual tip card (either on filtered or non-filtered results page), click “EDIT” button and verify that tip form fields get populated correctly with data from chosen tip.
    5. Try making changes to pre-populated fields and click “SAVE TIP” and verify that user is redirected to unfiltered results page and that the edited tip is included in results.
    6. OR try to click on “login” in main navigation, click on the “Read More” button on an individual tip card (either on filtered or non-filtered results page), click “DEL” button and verify that browser throws pop-up asking “Are you sure?”.
    7. Try clicking “OK” and verify that user is redirected to unfiltered results page and that the deleted tip was removed from results.
    8. OR try clicking on “Manage Categories” link in main navigation and verify that all current categories are listed incl. an “EDIT” and “DEL” button and “Add New Category” button below results.
    9. Try clicking EDIT” button and verify that category form field gets populated correctly with data from chosen category.
    10. Try making changes to pre-populated field and click “SAVE CATEGORY” and verify that user is redirected to unfiltered results page and that the edited tip is included in results.
    11. OR Try clicking “DEL” button and verify that browser throws pop-up asking “Are you sure?”.
    12. Try clicking “OK” and verify that user is redirected to categories page and that the deleted category was removed from results.

Manual testing revealed that adding, editing and deleting tips was integrated and visualised seamlessly. The functionality is accessible on all devices and all major browsers and looks virtually the same on different Browsers.





Only one minor bug was noticed when content on main page would not display correctly due to unclosed div tag. Bug fixed.





## Deployment






Uploaded project to github repository by using commands:

- git remote add origin https://github.com/Siminic87/user-centric-milestone-final.git

Followed by:

- git push -u origin master

in Cloud9's command line interface. Was then asked to enter username and password to confirm. Project now stored here: [https://github.com/Siminic87/user-centric-milestone-final](https://github.com/Siminic87/user-centric-milestone-final)

To run locally: [GitHub Pages](https://siminic87.github.io/user-centric-milestone-final/)

## Credits
### Media
