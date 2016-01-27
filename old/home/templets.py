# -*- coding: utf-8 -*-

#from django.template.base import Template, RequestContext  # Library, Node
#
#try:
#    from shpaml import convert_text
#except:
#    from shpaml.shpaml import convert_text
#
#from django_stylus.templatetags.stylus import compileit

from obdjects.templates import MinamlTemplate, StylusTemplate

from django.conf import settings


#### Site-wide styles - compiled to site.css

site_css = StylusTemplate('''\
// Globals, mixins, declarations, body, site-wide stuff

vertical-gradient(tp, bt)
    background-color tp
    background -webkit-gradient(linear, left top, left bottom, color-stop(0, tp), color-stop(1, bt)) no-repeat
    background -webkit-linear-gradient(top, tp 0%, bt 100%) no-repeat
    background -moz-linear-gradient(top, tp 0%, bt 100%) no-repeat
    background -ms-linear-gradient(top, tp 0%, bt 100%) no-repeat
    background -o-linear-gradient(top, tp 0%, bt 100%) no-repeat
    background linear-gradient(top, tp 0%, bt 100%) no-repeat

horz-gradient(l, r)
    background-color l
    background -webkit-gradient(linear, left top, right top, color-stop(0, l), color-stop(1, r)) no-repeat
    background -webkit-linear-gradient(left, l 0%, r 100%) no-repeat
    background -moz-linear-gradient(left, l 0%, r 100%) no-repeat
    background -ms-linear-gradient(left, l 0%, r 100%) no-repeat
    background -o-linear-gradient(left, l 0%, r 100%) no-repeat
    background linear-gradient(left, l 0%, r 100%) no-repeat

rad-gradient()
    background -moz-radial-gradient(arguments)
    background -ms-radial-gradient(arguments)
    background -o-radial-gradient(arguments)
    background -webkit-radial-gradient(arguments)
    background -khtml-radial-gradient(arguments)
    background radial-gradient(arguments)


// https://gist.github.com/1080346

vendor(prop, args)
    -webkit-{prop} args
    -moz-{prop} args
    -khtml-{prop} args
    -ms-{prop} args
    -o-{prop} args
    {prop} args

border-radius()
    vendor('border-radius', arguments)

box-shadow()
    vendor('box-shadow', arguments)

transition()
    vendor('transition', arguments)

transform()
    vendor('transform', arguments)

transform-origin()
    vendor('transform-origin', arguments)

user-select()
    vendor('user-select', arguments)


border-radius-old()
    -webkit-border-radius arguments
    -moz-border-radius arguments
    -khtml-border-radius arguments
    -ms-border-radius arguments
    -o-border-radius arguments
    border-radius arguments

rounded()
    -webkit-border-radius arguments
    -moz-border-radius arguments
    -khtml-border-radius arguments
    -ms-border-radius arguments
    -o-border-radius arguments
    border-radius arguments

rounded_bottom()
    -webkit-border-radius 0 0 arguments arguments
    -moz-border-radius 0 0 arguments arguments
    -khtml-border-radius 0 0 arguments arguments
    -ms-border-radius 0 0 arguments arguments
    -o-border-radius 0 0 arguments arguments
    border-radius 0 0 arguments arguments

rounded_top()
    -webkit-border-radius arguments arguments 0 0
    -moz-border-radius arguments arguments 0 0
    -khtml-border-radius arguments arguments 0 0
    -ms-border-radius arguments arguments 0 0
    -o-border-radius arguments arguments 0 0
    border-radius arguments arguments 0 0


true_columns(count, gap)
    vendor('column-count', count)
    vendor('column-gap', gap)

true_columns_old(count, gap)
    -moz-column-count    count
    -moz-column-gap      gap
    -webkit-column-count count
    -webkit-column-gap   gap
    -khtml-column-count  count
    -khtml-column-gap    gap
    -o-column-count      count
    -o-column-gap        gap
    -ms-column-count     count
    -ms-column-gap       gap
    column-count         count
    column-gap           gap


body
    vertical-gradient #000, white
    //vertical-gradient #00007c #7c0000 blue to crimson like letterman or Reno SC2007

.rounded
    rounded 8px

.rounded_bottom
    rounded_bottom 8px

.rounded_top
    rounded_top 8px

.flush_top
    margin-top 0

.flush_bottom
    margin-bottom 0

.row
    max-width 1200px

.hidden
    display none

// part of foundation.css, line 127
//
//.left
//    float left
//
//.right
//    float right

.bold, .highlighted
    font-weight bold


// Header stuff

.row#header
    ::comment
        vertical-gradient #ccf, white
    background: white

#logo
    padding 7px 15px

#page_top
    text-shadow 1px 1px 1px #666

#nav_small, #nav_login
    color lightgray
    a
        color lightgray
    a:hover
        color #EFE
    img
        vertical-align middle
        padding-left 5px

#nav_small, #mailing_list, #nav_login
    padding 10px 0

#mailing_list input
    font-size x-small
    display inline

#mailing_list input[type=button]
    padding 0

#mailing_list input[type=submit]
    padding 2px

#mailing_list form
    margin 0

#mailing_list i
    color #A9C790
//    color #86C751
//    color #799E5B
//    color #5b8737
//    color #8CC640

#header_right
    a
        padding 20px

    .skype img
        width 100px
        vertical-align middle

    #contactbox
        //border 3px solid orange
        //line-height 18px

        a
            padding 0

        table
            margin 0

            td
                //padding 0 10px
                padding 14px
                font-weight bold
                vertical-align middle
                img
                    margin-top -5px

#nav_account
    ::comment
        vertical-gradient #407095, #345B79
        vertical-gradient #ccf, white
        vertical-gradient #A9C790, white
    vertical-gradient #86B86B, #639548
    box-shadow 0px 3px 10px #888
    border 0
    height 30px
    li
        line-height 30px
        a
            color white

 /*
  * Main nav bar
  */

#nav_main
    margin-top 0
    .nav-bar
        margin-top 0
        height 30px
    height 30px
    line-height 30px
    .nav-bar li
        line-height 30px
    ul
        vertical-gradient #444, #222
    a
        color #DDD
        text-shadow 1px 1px 1px #666

    a:hover
        color #EFE
        text-shadow 1px 1px 1px #666
    form#search
        color #DDD
        text-shadow 1px 1px 1px #666
        padding 0 5px
        margin 0
        font-size 1.5rem
        input
            height 20px
            padding 1px
            margin 0
            font-size small
            display inline
    li:last-child
        float right


 /*
  * Home page featured items slider - Orbit
  */

#featured
    margin-top 20px
    width 610px
    height 396px
    //background gray url('/images/orbit/loading.gif') no-repeat center center
    //background gray url('/media/home/images/slideshow/front_nas50.jpeg') no-repeat center center
    background gray url('/media/home/images/slideshow/400tbnas50nov20.jpg') no-repeat center center
    overflow hidden

    img, div
        display none

#featured.orbit
    background none
    img, div
        display block

.orbit-wrapper .slider-nav span
    filter unquote("progid:DXImageTransform.Microsoft.Alpha(Opacity=0)")
    opacity 0
    -webkit-transition opacity 400ms
    -moz-transition opacity 400ms
    -o-transition opacity 400ms
    transition opacity 400ms

.orbit-wrapper:hover .slider-nav span
    filter unquote("progid:DXImageTransform.Microsoft.Alpha(Opacity=100)")
    opacity 1

ul.orbit-bullets
    bottom -10px


 /*
  * Checkout stuff - next, back buttons
  */

.errorlist
    color red

#cartform, #checkoutform
    margin-bottom 0

    ul, li, label
        margin-bottom 0

    table
        width 100%
        td
            padding 2px 10px
        th
            text-align center
            vertical-align middle
        tbody
            th
                width 20%
                text-align right
        thead
            th
                padding 4px 10px
                input[type=button], button
                    padding 1px 10px
            img
                vertical-align sub
        select
            width 250px
        textarea
            height 4em
            padding 2px
        input, textarea, select
            margin 0

    .expirydatefield select
        width 100px
        float left
        //display inline


#cartform #cart li
    list-style circle inside
    text-align left
    line-height 12px
    margin-bottom 5px


#confirmform, #final_cart
    table
        td
            padding 0 10px
        thead
            th
                text-align center
                padding 4px 10px
        ::comment
            border-collapse separate
            border 1px solid gray

#title_row
    rad-gradient #bdb, #eef

    h1
        background transparent
        padding-top 0
        margin-bottom 0

//background: -moz-radial-gradient(#00DD00, #DD00DD) repeat scroll 0 0 transparent;

#back, #next
    padding 20px

#back a, #next a, #back input, #next input
    background url('/images/orders/nav_back.png') no-repeat
    display block
    color white
    height 30px
    width 53px
    line-height 12px
    padding 2px 24px

#back a:hover, #back input:hover
    background url('/images/orders/nav_back_press.png') no-repeat

#next a, #next input
    background url('/images/orders/nav_next.png') no-repeat

#next a:hover, #next input:hover
    background url('/images/orders/nav_next_press.png') no-repeat

#back
    float left

#next
    float right

#cart
    .evenrow
        background white
    .oddrow
        background #D6F2BF
    th
        font-weight bold
        background lightblue
        border-bottom 1px solid lightgray

 /*
  * Login / Userena stuff
  */

#signin_signup_modal form
    border 2px red
    label
        margin-bottom 0

.white-box
    vertical-gradient #FFF, #CCC
    padding 10px
    #details
        font-size larger
#box-nav
    li
        display inline
    li a
        border 1px solid lightgray
        border-radius 3px 3px 3px 3px
        padding 5px
        margin 5px
        vertical-gradient #FFDCA8, #FFA858
        //#FF8000


 /*
  * Misc main content stuff
  */

.content img
    height auto!important

#content_row, #breadcrumbs_row
    background white

#os_logos a
    padding 0

ul.breadcrumbs
    padding 0 10px
    margin-bottom 0

ul.breadcrumbs li a, ul.breadcrumbs li span
    font-size normal
    text-transform none

#breadcrumbs_row div.social_link
    padding 0 10px

h1, h2
    padding-top 10px
    margin-top 10px

h1
    horz-gradient white, #8B9D54
    text-shadow 2px 2px 2px #666

 /*
  * Box & Product List
  */

.box
    border 1px solid #DDD
    h4
        font-size small
        vertical-gradient #444, #222
        padding 5px 20px
        color #DDD
        text-shadow 1px 1px 1px #666
        box-shadow 0px 10px 10px #888
        //border-bottom solid #5b8737 3px
        border-bottom solid #799E5B 3px
    ul.nav-bar
        border 0
        li
            width 100%
            border 0
            line-height 1em
        hr
            margin-top 15px

 /*
  * Product list
  */

#product_list
    ul.nav-bar
        margin-top 10px
        background transparent
    li
        background rgba(210, 210, 210, 0.3)
    .flyout
        left 100px
        top 20px
        padding 0
        vertical-gradient #FFF, #CCCFCC
        box-shadow 0px 10px 10px #888
        .hdr
            //width 100%
            //text-align center
            text-shadow 1px 1px 1px #999
            //border-bottom 1px solid #999
        hr
            margin 0 auto
    .flyout-toggle
        padding 12px
    li a.main
        //width 75%
        border-bottom 3px groove white
        margin auto
    li:last-child a.main
        border-bottom 0
    a, div
        line-height 25px


#config_summary
    .baseprice, .price
        font-size larger
    #current
        padding 12px
        line-height 24px
        li
            font-size smaller
            line-height 15px
            margin-bottom 5px
            list-style circle inside

#customers
    true_columns 4, 18px
    li
        display inline-block
        padding 20px
        a img
            max-width 180px
            width: 100%

.three_columns
    true_columns 3, 10px

 /*
  * Product config page
  */

.configgrid
    td
        padding-left 10px
        padding-right 10px
    td.dropdowns
        width 300px
    select
        //width 300px
        display inline
    select.choiceqty
        width 15%
    select.choiceid
        width 100%
    select.choiceid.leaveroom
        width 80%

 /*
  * Footer
  */

#footer
    vertical-gradient #DDD, #BBB
    border-collapse separate
    border-spacing 20px
    width 100%

    tr, td
        padding 0


.right-dotted
    border-right 2px dotted green

.vertical li hr
    width 75%!important
    margin-left auto
    margin-right auto

.text_center
    text-align center


''',
    destination = 'site.css',
)


#### Site-wide templates partials - compiled to home/templates/_<name>.html

nav_login = MinamlTemplate ('''\
    % load browserid
    % load staticfiles
    script type="text/javascript" src="https://code.jquery.com/jquery-1.8.0.min.js" ||
    script type="text/javascript" src="https://login.persona.org/include.js" ||
    script type="text/javascript" src="{% static 'browserid/api.js' %}" ||
    script type="text/javascript" src="{% static 'browserid/browserid.js' %}" ||

    nav id=nav_login
        Login with:
        a.browserid-login id=browserid href="#" title="Login with Mozilla Persona / BrowserID" data-next="{% if request.path == '/accounts/signout/' %}{{ request.META.HTTP_REFERER }}{% elif request.REQUEST.next %}{{ request.REQUEST.next }}{% else %}{{request.path}}{% endif %}"
            > img src="/images/logos/login/persona.png" height=24 width=24 alt="BrowserID / Persona login"
        ::comment
            a.browserid-login href="#" title="Login with Mozilla Persona / BrowserID"
                new examples sep 2013:
                % browserid_login text='' color='dark'

                {% if user.is_authenticated %}
                    {% browserid_logout text='Logout' %}
                {% else %}
                    {% browserid_login text='Login' color='dark' %}
                {% endif %}

                old:
                > img alt="BrowserID / Persona button" src="https://browserid.org/i/sign_in_orange.png"
                with Persona
            > img src="/images/logos/login/persona.png" height=24 width=24 alt="BrowserID / Persona login"
        a href="{% url 'social:begin' 'facebook' %}?next={{ request.path }}" title="Login with your Facebook account"
            > img src="/images/logos/login/facebook.png" height="24" width="24" alt="Facebook login"
        a href="{% url 'social:begin' 'twitter' %}" title="Login with your Twitter account"
            > img src="/images/logos/login/twitter.png" height="24" width="24" alt="Twitter login"
        a href="{% url 'social:begin' 'github' %}" title="Login with your Github account"
            > img src="/images/home/github-logo-48x48.png" height="24" width="24" alt="Github login"
        a href="{% url 'social:begin' 'linkedin' %}" title="Login with LinkedIn"
            > img src="/images/logos/login/linkedin.png" height="24" width="24" alt="LinkedIn login"
        a href="{% url 'social:begin' 'google-oauth2' %}" title="Login with Google"
            > img src="/images/logos/login/google.png" height="24" width="24" alt="Google+ login"
        a href="{% url 'social:begin' 'dropbox' %}" title="Login with your Dropbox account"
            > img src="/images/logos/login/dropbox.png" height="24" width="24" alt="Dropbox login"
        ::comment
            ·
            ·
    ''',
    destination = '_nav_login.html'
)


header_right = MinamlTemplate ('''\
    % load browserid
    % browserid_info
    #header_right
        .row
            .eight.columns.offset-by-three
                ul#nav_account.rounded_bottom.nav-bar.flush_top
                    %if user.is_authenticated
                        li
                            a href="{% url "userena_profile_detail" user.username %}" | {{ user.username }}'s Account
                        li
                            a href="{% url "userena_signout" %}" | Logout
                    %if not user.is_authenticated
                        li
                            a href=# data-reveal-id=signin_signup_modal | Login / Register
                            ::comment
                                %comment
                                    from django-browserid docs
                                <a id="browserid" href="{% url "userena_signin" %}">Sign In</a>
                            ::comment
                              <form method="POST" action="{% url "browserid_login" %}">
                                {% csrf_token %}
                                {{ browserid_form.as_p }}
                              </form>
                    li
                        a href='/cart/' title='Your Cart'
                            > img src='/images/orders/cart.gif' alt='Cart' title="Your Cart"
                            %if cart_totqty
                                =cart_totqty
                                items, $
                                =cart_grandtot|floatformat:2
                            %if not cart_totqty
                                (Empty)
                    ::comment
                        %if cart_totqty
                            li
                                a href='/checkout/' title="Checkout" | Checkout
        .row
            .seven.columns
                =os_logos
            .four.columns#contactbox
                table
                    tr
                        td
                            eMail:
                        td
                            a href=mailto:info@eracks.com | info@eracks.com
                    ::comment
                        tr
                            td
                                Phone:
                            td
                                a href=call:714-758-5423 | 714-758-5423
                        tr
                            td
                                Skype:
                            td.skype
                                =skype_widget
            .one.column
                &nbsp;
    ''',
    destination = '_header_right.html'
)


nav_main = MinamlTemplate ('''\
nav#nav_main
    ul.nav-bar
        li
            a.main href="/products/" title="eRacks Product Showroom" | Products
        li
            a.main href="/services/" title="eRacks Services" | Services
        li
            a.main href="/partners/" title="eRacks Partners" | Partners
        li
            a.main href="/customers/" title="eRacks Customers and Testimonials" | Customers
        ::comment
            li
                a.main href="/faq/" title="eRacks Frequently Asked Questions" | FAQ
        li
            a.main href="/press/" title="News about eRacks, Press Releases" | Press
        li
            a.main href="/corporate/" title="About eRacks" | About Us
        li
            a.main href="http://blog.eracks.com/" title="eRacks Tech News and Blog" | Blog
        li
            a.main href="{% url 'contact' %}" title="Contact eRacks" | Contact Us
        li
            form#search class=nice action=/search/
                Search
                > input type=search class="small input-text" placeholder="Enter search text" name=q
                > input type=submit class="nice small radius red button" value=GO
    ''',
    destination = '_nav_main.html'
)


breadcrumbs = MinamlTemplate ('''\
    <ul class="breadcrumbs">
        <li><a href="/" title="eRacks Home Page">Home</a></li>
        %for bc in breadcrumbs
            li
                a href="{{ bc.url }}" title="{{ bc.title }}"
                    =bc.name
    </ul>
    ''',
    destination = '_breadcrumbs.html'
)


fat_footer = MinamlTemplate ('''\
    .row
        .twelve.columns
            table#footer
                tr
                    td.right-dotted
                        h5 | eRacks Info
                        div | <a href="/rackmount-servers">Rackmount Server Basics</a>
                        div | <a href="/open-source-links/">Open source Links</a>
                        div
                            a.main href="/faq/" title="eRacks Frequently Asked Questions" | Frequently Asked Questions
                        div
                            a.main href="/corporate/" title="About eRacks" | About Us
                        div
                            a.main href="/contact-us/" title="Contact eRacks" | Contact Us
                        div
                            a.main href="/jobs/" title="Positions at eRacks" | Gigs / Jobs

                    td.right-dotted
                        h5 | eRacks Business
                        div
                            a.main href="/showroom/" title="eRacks Product Showroom" | Products
                        div
                            a.main href="/services/" title="eRacks Services" | Services
                        div
                            a.main href="/partners/" title="eRacks Partners" | Partners
                        div
                            a.main href="/customers/" title="eRacks Customers and Testimonials" | Customers
                        div
                            a.main href="/press/" title="News about eRacks, Press Releases" | Press
                    td.right-dotted
                        h5 | eRacks Misc
                        div
                            a.main href="http://blog.eracks.com/" title="eRacks Tech News and Blog" | Blog
                        div
                            a.main href="http://accessories.eracks.com/" title="eRacks Computer parts and Accessories, notebooks, tablets, etc" | Accessories
                        div
                            a.main href="http://studio.eracks.com/" title="eRacks Studio and Music-related Blog" | Studio / Music Blog
                        div
                            a.main href="/policies/privacy-and-legal" | Privacy, Legal Policies
                        div
                            a.main href="/policies/warranty-and-order" | Warranty & Order Policies

                    %if request.user.is_staff
                        td.right-dotted
                            h5 | eRacks Admin
                            div
                                a href="/admin/" | Admin
                            div
                                a href="/djide/" | Django IDE
                            div
                                a href="/admin/home/featuredimage/" | Featured Images
                            div
                                a href="/admin/auth/user/{{ request.user.id }}/"
                                    User:
                                    =request.user
                            %if product
                                div
                                    a href="/admin/products/product/{{ product.id }}/"
                                        Edit Product:
                                        =product
                            %if category
                                div
                                    a href="/admin/products/categories/{{ category.id }}/"
                                        Edit Category:
                                        =category
                            %if settings.ALOHA
                                div
                                    a href="?edit=1" | Edit in place
                            %if settings.DEBUG
                                div
                                    a href="/packages/" | Packages directory
                            div
                                a href="/utils/clearcache/" | Clear cache
                            div
                                a href="/utils/collect_static/" | Collect Static
                            div
                                a href="/utils/urls/" | Show URL map
                            div
                                a href="/session/" | Show Session

                    td
                        h5 | Accreditations
                        div
                            =bbb_horizontal
                        div
                            =trustwave_siteseal
                        div
                            =geotrust_seal
    .row
        div.text_center
            a href=http://eracks.com title="Top-quality rackmount servers"
                > img src=/images/logos/smalle.gif alt=small-e
            > br
            eRacks Open Source Systems © Copyright 1999-2013, All rights reserved.
            > br
            Powered by the best
            a href= http://eracks.com | rackmount servers
            from eRacks Open Source Systems
            > br
    ''',

    destination = '_footer.html'
)


#### Home page-specific whole-page template, generated and saved to home.html

home_page = MinamlTemplate ('''\
    %extends "base.html"
    %load cache

    %block css
        =block.super
        <!--[if IE]>
            <style type="text/css">
                .timer { display: none !important; }
                div.caption { background:transparent; filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#99000000,endColorstr=#99000000);zoom: 1; }
            </style>
        <![endif]-->

    %block content
        =block.super

        %cache 3600 featured_images
            #featured
                %for f in featured_images
                    = f.as_content
            %for f in featured_images
                = f.as_caption

        .panel.five.columns
            =home_page_text_1

        .panel.five.columns.right
            =home_page_text_2

        .panel.eleven.columns
            =home_page_text_3

        .one.column | &nbsp;

    %block js_bottom
        script type="text/javascript" VERBATIM
            $(window).load(function() {
                $('#featured').orbit({
                    bullets: true,              // true or false to activate the bullet navigation
                    captions: true,             // 'Captions' are really html overlay
                    directionalNav: false,      // manual advancing directional navs
                    fluid: '305x198',           // half of 610x396
                });
            });
        =block.super

        ::comment
            /* no longer needed, linked directly in html
            $('#featured img').each (function() {
                //console.log ($(this).attr('data_link'));
                $(this).click (function (e) {
                    //console.log ($(this));
                    location.href = $(this).attr('data_link');
                });
            });
            */
    ''',

    destination = 'home.html'  # puts in app dir autommatically for relative templates dir
    # Do this for global tproject emplates dir:
    # destination = settings.PROJECT_ROOT + '/templates/home.html'
)

#### Contact Page, generated and saved to contact.html
contact_page = MinamlTemplate('''\
%extends "base.html"
%load i18n
%block content
    {{ block.super }}
    h1 | Contact eRacks
    p | Customized rackmount and desktop systems are our specialty! We frequently put configurations together for customers that have unique requirements. Contact us today.
    p | Need network design help?
    p | Open Source enterprise migration services?
    p | eRacks experts can make special arrangements to tackle your design problems. Tell us about your project.
    form action=''  method='post'
        %csrf_token
        fieldset
            {{ form.non_field_errors }}
            %for field in form
                {{ field.errors }}
                {% comment %} Displaying checkboxes differently {% endcomment %}
                p  | {{ field.label_tag }} {{ field }}
        > input#contact  type=submit value='Submit'

    > img alt="" border="0" height="306" src="/images/contact-us/bcard_hand.gif" width="400"


    address
        strong  | eRacks Open Source Systems
        > br
        Has offices in:
    address
        &nbsp;- Fremont, CA
    address
        &nbsp;- Los Gatos, CA
    > br
    p
        b  | Phone: (714) 758-5423
        (Voicemail)
        > br
        Fax: (631) 392-9842
    p
        eMail:
        a  href=mailto:info@eracks.com | info@eracks.com
    p
        Twitter:
        a  href=http://twitter.com/eracks target=new | twitter.com/eracks
    p
        script src=http://download.skype.com/share/skypebuttons/js/skypeCheck.js style={} type=text/javascript
            ::comment
                empty
        a  href=skype:erackssales?call
            > img src=http://download.skype.com/share/skypebuttons/buttons/call_blue_transparent_70x23.png style="{u'border': u'none'}" height=23 width=70 alt="Skype Me !"
        > br
        Skype: erackssales

    ''',
    destination = 'contact.html'
    )


orbit_featured_options='''
$('#featured').orbit({

New sep 2012 foundation 2.2.1:

      animation: 'horizontal-push',     // fade, horizontal-slide, vertical-slide, horizontal-push, vertical-push
      animationSpeed: 600,        // how fast animtions are
      timer: true,            // true or false to have the timer
      advanceSpeed: 4000,         // if timer is enabled, time between transitions
      pauseOnHover: false,        // if you hover pauses the slider
      startClockOnMouseOut: false,    // if clock should start on MouseOut
      startClockOnMouseOutAfter: 1000,  // how long after MouseOut should the timer start again
      directionalNav: true,         // manual advancing directional navs
      directionalNavRightText: 'Right', // text of right directional element for accessibility
      directionalNavLeftText: 'Left', // text of left directional element for accessibility
      captions: true,           // do you want captions?
      captionAnimation: 'fade',       // fade, slideOpen, none
      captionAnimationSpeed: 600,     // if so how quickly should they animate in
      resetTimerOnClick: false,      // true resets the timer instead of pausing slideshow progress on manual navigation
      bullets: false,           // true or false to activate the bullet navigation
      bulletThumbs: false,        // thumbnails for the bullets
      bulletThumbLocation: '',      // location from this file where thumbs will be
      afterSlideChange: $.noop,   // empty function
      afterLoadComplete: $.noop, //callback to execute after everything has been loaded
      fluid: true,
      centerBullets: true,   // center bullet nav with js, turn this off if you want to position the bullet nav manually
      singleCycle: false     // cycles through orbit slides only once

old:
     animation: 'fade',             // fade, horizontal-slide, vertical-slide, horizontal-push
     animationSpeed: 800,           // how fast animtions are
     timer: true,                   // true or false to have the timer
     advanceSpeed: 4000,            // if timer is enabled, time between transitions
     pauseOnHover: false,           // if you hover pauses the slider
     startClockOnMouseOut: false,    // if clock should start on MouseOut
     startClockOnMouseOutAfter: 1000, // how long after MouseOut should the timer start again
     directionalNav: true,          // manual advancing directional navs
     captions: true,                // do you want captions?
     captionAnimation: 'fade',      // fade, slideOpen, none
     captionAnimationSpeed: 800,    // if so how quickly should they animate in
     bullets: false,                // true or false to activate the bullet navigation
     bulletThumbs: false,           // thumbnails for the bullets
     bulletThumbLocation: '',       // location from this file where thumbs will be
     afterSlideChange: function(){}, // empty function
     fluid: true                    // or set a aspect ratio for content slides (ex: '4x3')
});
'''


#### Old & OUttakes:

"""
        //<li class="unavailable"><a href="#">Gene Splicing</a></li>
        //<li class="current"><a href="#">Home</a></li>

look for OOB syntax-highlighting text to insert here

StylusTemplate ('''\
<style type="text/css">
test {
    background:
}
</style>
''')
"""

'''
# TODO: Finalize 3-column view w/images & caption

content = Template (convert_text ('' '
% extends "base-aloha.html"

.content#featured"
     <img src="overflow.jpg" alt="Overflow: Hidden No More" />
     <img src="captions.jpg"  alt="HTML Captions" />
     <img src="features.jpg" alt="and more features" />



% block js_bottom
  <script type="text/javascript">
     $(window).load(function() {
         $('#featured').orbit();
     });
  </script>

'''

old_footer_attempts='''
    .row
        .twelve.columns#footer
            ul.block-grid.mobile.five-up
                li.right-dotted
                    div
                        strong
                            eRacks Info
                    div | <a href="/rackmount-servers">Rackmount Server Basics</a>
                    div | <a href="/links.html">Open source Links</a>
                    div | <a href="/faq">Frequently Asked Questions</a>
                    div | <a href="/corporate">About eRacks</a>
                    div | <a href="/contact">Contact eRacks</a>
                    div | <a href="/policies">Privacy, Warranty, Legal</a>

                li.right-dotted
                    Column two
                li.right-dotted
                    Column three
                li.right-dotted
                    Column four
                li
                    Column five

        .three.columns.right-dotted
            div
                strong
                    eRacks Info
            div | <a href="/rackmount-servers">Rackmount Server Basics</a>
            div | <a href="/links.html">Open source Links</a>
            div | <a href="/faq">Frequently Asked Questions</a>
            div | <a href="/corporate">About eRacks</a>
            div | <a href="/contact">Contact eRacks</a>
            div | <a href="/policies">Privacy, Warranty, Legal</a>

        .three.columns.right-dotted
            Column two
        .three.columns.right-dotted
            Column three
        .three.columns
            Column four
'''

