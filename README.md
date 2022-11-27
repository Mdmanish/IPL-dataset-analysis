<!DOCTYPE html>
<!-- saved from url=(0097)https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md -->
<html class="" lang="en"><head prefix="og: http://ogp.me/ns#"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Edit · README.md · main · mountblue / Cohort 22 Python / Manish / IPL data set analytics · GitLab</title>
<link rel="preload" href="./README_files/application_utilities-6e21d68b1ca9da299256cfb26f7422439a6d11822c228fc18238d1c7d737f1df.css" as="style" type="text/css" nonce="">
<link rel="preload" href="./README_files/application-7ac3b54e2ee2a129462d6702c9857a04f1a405f7254b89a2b3dfc7e73e80a489.css" as="style" type="text/css" nonce="">
<link rel="preload" href="./README_files/white-925931f55f1eb5f0fdef8460d44b95748a47b6d0ecf3e9a50587f3686ff7c5bd.css" as="style" type="text/css" nonce="">
<link crossorigin="" href="https://snowplow.trx.gitlab.net/" rel="preconnect">

<meta content="IE=edge" http-equiv="X-UA-Compatible">

<link rel="preload" href="./README_files/monaco.a6d661ed.chunk.js" as="script" type="text/javascript" nonce="">
<link rel="shortcut icon" type="image/png" href="https://gitlab.com/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png">
<style>
@keyframes blinking-dot{0%{opacity:1}25%{opacity:0.4}75%{opacity:0.4}100%{opacity:1}}@keyframes blinking-scroll-button{0%{opacity:0.2}50%{opacity:1}100%{opacity:0.2}}@keyframes gl-spinner-rotate{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}body.ui-indigo{--gl-theme-accent: #6666c4}body.ui-indigo .navbar-gitlab{background-color:#292961}body.ui-indigo .navbar-gitlab .navbar-collapse{color:#d1d1f0}body.ui-indigo .navbar-gitlab .container-fluid .navbar-toggler{border-left:1px solid #6868b9;color:#d1d1f0}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>a:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>a:focus,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>button:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>button:focus,body.ui-indigo .navbar-gitlab .navbar-nav>li>a:hover,body.ui-indigo .navbar-gitlab .navbar-nav>li>a:focus,body.ui-indigo .navbar-gitlab .navbar-nav>li>button:hover,body.ui-indigo .navbar-gitlab .navbar-nav>li>button:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.active>a,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.active>button,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.dropdown.show>a,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.dropdown.show>button,body.ui-indigo .navbar-gitlab .navbar-nav>li.active>a,body.ui-indigo .navbar-gitlab .navbar-nav>li.active>button,body.ui-indigo .navbar-gitlab .navbar-nav>li.dropdown.show>a,body.ui-indigo .navbar-gitlab .navbar-nav>li.dropdown.show>button{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.line-separator,body.ui-indigo .navbar-gitlab .navbar-nav>li.line-separator{border-left:1px solid rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li.header-search-new{color:#333238}body.ui-indigo .navbar-gitlab .nav>li>a .notification-dot{border:2px solid #292961}body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle .notification-dot{background-color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li>a.header-user-dropdown-toggle .header-user-avatar{border-color:#d1d1f0}@media (min-width: 576px){body.ui-indigo .navbar-gitlab .nav>li>a:hover,body.ui-indigo .navbar-gitlab .nav>li>a:focus{background-color:rgba(209,209,240,0.2)}}body.ui-indigo .navbar-gitlab .nav>li>a:hover svg,body.ui-indigo .navbar-gitlab .nav>li>a:focus svg{fill:currentColor}body.ui-indigo .navbar-gitlab .nav>li>a:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav>li>a:focus .notification-dot{will-change:border-color, background-color;border-color:#4a4a82}body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle:focus .notification-dot{background-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a:hover svg,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a:hover svg{fill:#292961}body.ui-indigo .navbar-gitlab .nav>li.active>a .notification-dot,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a .notification-dot{border-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a.header-help-dropdown-toggle .notification-dot,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a.header-help-dropdown-toggle .notification-dot{background-color:#292961}body.ui-indigo .navbar-gitlab .nav>li .impersonated-user svg,body.ui-indigo .navbar-gitlab .nav>li .impersonated-user:hover svg{fill:#292961}body.ui-indigo .navbar .title>a:hover,body.ui-indigo .navbar .title>a:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .header-search{background-color:rgba(209,209,240,0.2) !important;border-radius:4px}body.ui-indigo .header-search:hover{background-color:rgba(209,209,240,0.3) !important}body.ui-indigo .header-search svg.gl-search-box-by-type-search-icon{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input{background-color:transparent;color:rgba(209,209,240,0.8);box-shadow:inset 0 0 0 1px rgba(209,209,240,0.4)}body.ui-indigo .header-search input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input:focus::placeholder,body.ui-indigo .header-search input:active::placeholder{color:#89888d}body.ui-indigo .header-search .keyboard-shortcut-helper{color:#d1d1f0;background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form{background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form:hover{background-color:rgba(209,209,240,0.3)}body.ui-indigo .search .search-input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .search .search-input-wrap .search-icon,body.ui-indigo .search .search-input-wrap .clear-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .search.search-active form{background-color:#fff}body.ui-indigo .search.search-active .search-input-wrap .search-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .search-sidebar .nav-link.active,body.ui-indigo .search-sidebar .nav-link:hover{background-color:rgba(236,236,239,0.8);color:#333238}body.ui-indigo .nav-sidebar li.active>a{color:#333238}body.ui-indigo .nav-sidebar .fly-out-top-item a,body.ui-indigo .nav-sidebar .fly-out-top-item a:hover,body.ui-indigo .nav-sidebar .fly-out-top-item.active a,body.ui-indigo .nav-sidebar .fly-out-top-item .fly-out-top-item-container{background-color:var(--gray-100, #ececef);color:var(--gray-900, #333238)}body.ui-indigo .branch-header-title{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active.is-right{box-shadow:inset -3px 0 #4b4ba3}

*,*::before,*::after{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15}aside,header{display:block}body{margin:0;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:1rem;font-weight:400;line-height:1.5;color:#333238;text-align:left;background-color:#fff}ul{margin-top:0;margin-bottom:1rem}ul ul{margin-bottom:0}strong{font-weight:bolder}a{color:#1f75cb;text-decoration:none;background-color:transparent}a:not([href]):not([class]){color:inherit;text-decoration:none}kbd{font-family:"Menlo", "DejaVu Sans Mono", "Liberation Mono", "Consolas", "Ubuntu Mono", "Courier New", "andale mono", "lucida console", monospace;font-size:1em}img{vertical-align:middle;border-style:none}svg{overflow:hidden;vertical-align:middle}button{border-radius:0}input,button{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button{text-transform:none}[role="button"]{cursor:pointer}button:not(:disabled),[type="button"]:not(:disabled){cursor:pointer}button::-moz-focus-inner,[type="button"]::-moz-focus-inner{padding:0;border-style:none}[type="search"]{outline-offset:-2px}.list-unstyled{padding-left:0;list-style:none}kbd{padding:0.2rem 0.4rem;font-size:90%;color:#fff;background-color:#333238;border-radius:0.2rem}kbd kbd{padding:0;font-size:100%;font-weight:600}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.form-control{display:block;width:100%;height:34px;padding:0.375rem 0.75rem;font-size:0.875rem;font-weight:400;line-height:1.5;color:#333238;background-color:#fff;background-clip:padding-box;border:1px solid #89888d;border-radius:0.25rem}.form-control:-moz-focusring{color:transparent;text-shadow:0 0 0 #333238}.form-control::placeholder{color:#626168;opacity:1}.form-control:disabled{background-color:#fbfafd;opacity:1}.form-inline{display:flex;flex-flow:row wrap;align-items:center}@media (min-width: 576px){.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}}.btn{display:inline-block;font-weight:400;color:#333238;text-align:center;vertical-align:middle;-webkit-user-select:none;user-select:none;background-color:transparent;border:1px solid transparent;padding:0.375rem 0.75rem;font-size:1rem;line-height:20px;border-radius:0.25rem}.btn:disabled{opacity:0.65}.btn:not(:disabled):not(.disabled){cursor:pointer}.collapse:not(.show){display:none}.dropdown{position:relative}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:10rem;padding:0.5rem 0;margin:0.125rem 0 0;font-size:1rem;color:#333238;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,0.15);border-radius:0.25rem}.nav{display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.navbar{position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:0.25rem 0.5rem}.navbar .container-fluid{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between}.navbar-nav{display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:0.25rem 0.75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:0.25rem}@media (max-width: 575.98px){.navbar-expand-sm>.container-fluid{padding-right:0;padding-left:0}}@media (min-width: 576px){.navbar-expand-sm{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm>.container-fluid{flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:flex !important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}}.badge{display:inline-block;padding:0.25em 0.4em;font-size:75%;font-weight:600;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:0.25rem}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.badge-pill{padding-right:0.6em;padding-left:0.6em;border-radius:10rem}.badge-success{color:#fff;background-color:#108548}.badge-info{color:#fff;background-color:#1f75cb}.badge-warning{color:#fff;background-color:#ab6100}.rounded-circle{border-radius:50% !important}.d-none{display:none !important}.d-block{display:block !important}@media (min-width: 576px){.d-sm-none{display:none !important}.d-sm-inline-block{display:inline-block !important}}@media (min-width: 768px){.d-md-block{display:block !important}}@media (min-width: 992px){.d-lg-none{display:none !important}}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border:0}.gl-avatar{border-width:1px;border-style:solid;border-color:rgba(31,30,36,0.08);overflow:hidden;flex-shrink:0}.gl-avatar-s24{width:1.5rem;height:1.5rem;font-size:0.75rem;line-height:1rem;border-radius:0.25rem}.gl-avatar-circle{border-radius:50%}.gl-badge{display:inline-flex;align-items:center;font-size:0.75rem;font-weight:400;line-height:1rem;padding-top:0.25rem;padding-bottom:0.25rem;padding-left:0.5rem;padding-right:0.5rem}.gl-badge.sm{padding-top:0;padding-bottom:0}.gl-badge.badge-info{background-color:#cbe2f9;color:#0b5cad}a.gl-badge.badge-info.active,a.gl-badge.badge-info:active{color:#033464;background-color:#9dc7f1}a.gl-badge.badge-info:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-badge.badge-success{background-color:#c3e6cd;color:#24663b}a.gl-badge.badge-success.active,a.gl-badge.badge-success:active{color:#0a4020;background-color:#91d4a8}a.gl-badge.badge-success:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-badge.badge-warning{background-color:#f5d9a8;color:#8f4700}a.gl-badge.badge-warning.active,a.gl-badge.badge-warning:active{color:#5c2900;background-color:#e9be74}a.gl-badge.badge-warning:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-button .gl-badge{top:0}.gl-form-input,.gl-form-input.form-control{background-color:#fff;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:0.875rem;line-height:1rem;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;height:auto;color:#333238;box-shadow:inset 0 0 0 1px #89888d;border-style:none;-webkit-appearance:none;appearance:none;-moz-appearance:none}.gl-form-input:disabled,.gl-form-input:not(.form-control-plaintext):not([type="color"]):read-only,.gl-form-input.form-control:disabled,.gl-form-input.form-control:not(.form-control-plaintext):not([type="color"]):read-only{background-color:#fbfafd;box-shadow:inset 0 0 0 1px #dcdcde}.gl-form-input:disabled,.gl-form-input.form-control:disabled{cursor:not-allowed;color:#737278}.gl-form-input::placeholder,.gl-form-input.form-control::placeholder{color:#89888d}.gl-icon{fill:currentColor}.gl-icon.s12{width:12px;height:12px}.gl-icon.s16{width:16px;height:16px}.gl-icon.s32{width:32px;height:32px}.gl-link{font-size:0.875rem;color:#1f75cb}.gl-link:active{color:#0b5cad}.gl-link:active{text-decoration:underline;outline:2px solid #428fdc;outline-offset:2px}.gl-button{display:inline-flex}.gl-button:not(.btn-link):active{text-decoration:none}.gl-button.gl-button{border-width:0;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;background-color:transparent;line-height:1rem;color:#333238;fill:currentColor;box-shadow:inset 0 0 0 1px #bfbfc3;justify-content:center;align-items:center;font-size:0.875rem;border-radius:0.25rem}.gl-button.gl-button.btn-default{background-color:#fff}.gl-button.gl-button.btn-default:active,.gl-button.gl-button.btn-default.active{box-shadow:inset 0 0 0 1px #626168, 0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none;background-color:#dcdcde}.gl-button.gl-button.btn-default:active .gl-icon,.gl-button.gl-button.btn-default.active .gl-icon{color:#333238}.gl-button.gl-button.btn-default .gl-icon{color:#737278}.gl-search-box-by-type-search-icon{margin:0.5rem;color:#737278;width:1rem;position:absolute}.gl-search-box-by-type{display:flex;position:relative}.gl-search-box-by-type-input,.gl-search-box-by-type-input.gl-form-input{height:2rem;padding-right:2rem;padding-left:1.75rem}body{font-size:0.875rem}button,html [type="button"],[role="button"]{cursor:pointer}strong{font-weight:bold}svg{vertical-align:baseline}.form-control,.search form{font-size:0.875rem}.hidden{display:none !important;visibility:hidden !important}.hide{display:none}.badge:not(.gl-badge){padding:4px 5px;font-size:12px;font-style:normal;font-weight:400;display:inline-block}.divider{height:0;margin:4px 0;overflow:hidden;border-top:1px solid #dcdcde}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left{color:#737278}html{overflow-y:scroll}@media (min-width: 576px){.logged-out-marketing-header{--header-height: 72px}}.btn{border-radius:4px;font-size:0.875rem;font-weight:400;padding:6px 10px;background-color:#fff;border-color:#dcdcde;color:#333238;color:#333238;white-space:nowrap}.btn:active{background-color:#ececef;box-shadow:none}.btn:active,.btn.active{background-color:#eaeaea;border-color:#e3e3e3;color:#333238}.btn svg{height:15px;width:15px}.btn svg:not(:last-child){margin-right:5px}.badge.badge-pill:not(.gl-badge){font-weight:400;background-color:rgba(0,0,0,0.07);color:#535158;vertical-align:baseline}.gl-font-sm{font-size:12px}.dropdown{position:relative}.dropdown-menu-toggle:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.search-input-container .dropdown-menu{margin-top:11px}.dropdown-menu-toggle{padding:6px 8px 6px 10px;background-color:#fff;color:#333238;font-size:14px;text-align:left;border:1px solid #dcdcde;border-radius:0.25rem;white-space:nowrap}.dropdown-menu-toggle.no-outline{outline:0}.dropdown-menu-toggle.dropdown-menu-toggle{justify-content:flex-start;overflow:hidden;padding-right:25px;position:relative;text-overflow:ellipsis;width:160px}.dropdown-menu{display:none;position:absolute;width:auto;top:100%;z-index:300;min-width:240px;max-width:500px;margin-top:4px;margin-bottom:24px;font-size:0.875rem;font-weight:400;padding:8px 0;background-color:#fff;border:1px solid #dcdcde;border-radius:0.25rem;box-shadow:0 2px 4px rgba(0,0,0,0.1)}.dropdown-menu ul{margin:0;padding:0}.dropdown-menu li{display:block;text-align:left;list-style:none}.dropdown-menu li>a,.dropdown-menu li button{background:transparent;border:0;border-radius:0;box-shadow:none;display:block;font-weight:400;position:relative;padding:8px 12px;color:#333238;line-height:16px;white-space:normal;overflow:hidden;text-align:left;width:100%}.dropdown-menu li>a:active,.dropdown-menu li button:active{background-color:#ececef;color:#333238;outline:0;text-decoration:none}.dropdown-menu li>a:active,.dropdown-menu li button:active{box-shadow:inset 0 0 0 2px #428fdc, inset 0 0 0 3px #fff, inset 0 0 0 1px #fff;outline:none}.dropdown-menu .divider{height:1px;margin:0.25rem 0;padding:0;background-color:#dcdcde}.dropdown-menu .badge.badge-pill+span:not(.badge):not(.badge-pill){margin-right:40px}@media (max-width: 575.98px){.navbar-gitlab li.dropdown{position:static}.navbar-gitlab li.dropdown.user-counter{margin-left:8px !important}.navbar-gitlab li.dropdown.user-counter>a{padding:0 4px !important}header.navbar-gitlab .dropdown .dropdown-menu{width:100%;min-width:100%}}@media (max-width: 767.98px){.dropdown-menu-toggle.dropdown-menu-toggle{width:100%}}input{border-radius:0.25rem;color:#333238;background-color:#fff}.form-control{border-radius:4px;padding:6px 10px}.form-control::placeholder{color:#89888d}kbd{display:inline-block;padding:3px 5px;font-size:0.6875rem;line-height:10px;color:var(--gray-700, #535158);vertical-align:middle;background-color:var(--gray-10, #fbfafd);border-width:1px;border-style:solid;border-color:var(--gray-100, #dcdcde) var(--gray-100, #dcdcde) var(--gray-200, #bfbfc3);border-image:none;border-radius:3px;box-shadow:0 -1px 0 var(--gray-200, #bfbfc3) inset}.navbar-gitlab{padding:0 16px;z-index:1000;margin-bottom:0;min-height:var(--header-height, 48px);border:0;position:fixed;top:0;left:0;right:0;border-radius:0}.navbar-gitlab .close-icon{display:none}.navbar-gitlab .header-content{width:100%;display:flex;justify-content:space-between;position:relative;min-height:var(--header-height, 48px);padding-left:0}.navbar-gitlab .header-content .title{padding-right:0;color:currentColor;display:flex;position:relative;margin:0;font-size:18px;vertical-align:top;white-space:nowrap}.navbar-gitlab .header-content .title img{height:24px}.navbar-gitlab .header-content .title a:not(.canary-badge){display:flex;align-items:center;padding:2px 8px;margin:4px 2px 4px -8px;border-radius:4px}.navbar-gitlab .header-content .title a:not(.canary-badge):active{box-shadow:0 0 0 1px rgba(0,0,0,0.6),0 0 0 3px #63a6e9;outline:none}.navbar-gitlab .header-content .navbar-collapse>ul.nav>li:not(.d-none){margin:0 2px}.navbar-gitlab .navbar-collapse{flex:0 0 auto;border-top:0;padding:0}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse{flex:1 1 auto}}.navbar-gitlab .navbar-collapse .nav{flex-wrap:nowrap}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse .nav>li:not(.d-none) a{margin-left:0}}.navbar-gitlab .container-fluid{padding:0}.navbar-gitlab .container-fluid .user-counter svg{margin-right:3px}.navbar-gitlab .container-fluid .navbar-toggler{position:relative;right:-10px;border-radius:0;min-width:45px;padding:0;margin:8px 8px 8px 0;font-size:14px;text-align:center;color:currentColor}.navbar-gitlab .container-fluid .navbar-toggler.active{color:currentColor;background-color:transparent}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .navbar-nav{display:flex;padding-right:10px;flex-direction:row}}.navbar-gitlab .container-fluid .navbar-nav li .badge.badge-pill:not(.gl-badge){box-shadow:none;font-weight:600}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav>li.header-user{padding-left:10px}}.navbar-gitlab .container-fluid .nav>li>a{will-change:color;margin:4px 0;padding:6px 8px;height:32px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav>li>a{padding:0}}.navbar-gitlab .container-fluid .nav>li>a.header-user-dropdown-toggle{margin-left:2px}.navbar-gitlab .container-fluid .nav>li>a.header-user-dropdown-toggle .header-user-avatar{margin-right:0}.navbar-gitlab .container-fluid .nav>li .header-new-dropdown-toggle{margin-right:0}.navbar-sub-nav>li>a,.navbar-sub-nav>li>button,.navbar-nav>li>a,.navbar-nav>li>button{display:flex;align-items:center;justify-content:center;padding:6px 8px;margin:4px 2px;font-size:12px;color:currentColor;border-radius:4px;height:32px;font-weight:600}.navbar-sub-nav>li>a:active,.navbar-sub-nav>li>button:active,.navbar-nav>li>a:active,.navbar-nav>li>button:active{box-shadow:0 0 0 1px rgba(0,0,0,0.6),0 0 0 3px #63a6e9;outline:none}.navbar-sub-nav>li .top-nav-toggle,.navbar-sub-nav>li>button,.navbar-nav>li .top-nav-toggle,.navbar-nav>li>button{background:transparent;border:0}.navbar-sub-nav .dropdown-menu,.navbar-nav .dropdown-menu{position:absolute}.navbar-sub-nav{display:flex;align-items:center;height:100%;margin:0 0 0 6px}.caret-down,.btn .caret-down{top:0;height:11px;width:11px;margin-left:4px;fill:currentColor}.header-user .dropdown-menu,.header-new .dropdown-menu{margin-top:4px}.btn-sign-in{background-color:#ebebfa;color:#292961;font-weight:600;line-height:18px;margin:4px 0 4px 2px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid{font-size:18px}.navbar-gitlab .container-fluid .navbar-nav{table-layout:fixed;width:100%;margin:0;text-align:right}.navbar-gitlab .container-fluid .navbar-collapse{margin-left:-8px;margin-right:-10px}.navbar-gitlab .container-fluid .navbar-collapse .nav>li:not(.d-none){flex:1}.header-user-dropdown-toggle{text-align:center}.header-user-avatar{float:none}}.header-user-avatar{float:left;margin-right:5px;border-radius:50%;border:1px solid #f2f2f4}.notification-dot{background-color:#d99530;height:12px;width:12px;pointer-events:none;visibility:hidden;top:3px}.tanuki-logo .tanuki{fill:#e24329}.tanuki-logo .left-cheek,.tanuki-logo .right-cheek{fill:#fc6d26}.tanuki-logo .chin{fill:#fca326}.context-header{position:relative;margin-right:2px;width:256px}.context-header>a,.context-header>button{font-weight:600;display:flex;width:100%;align-items:center;padding:10px 16px 10px 10px;color:#333238;background-color:transparent;border:0;text-align:left}.context-header .avatar-container{flex:0 0 32px;background-color:#fff}.context-header .sidebar-context-title{overflow:hidden;text-overflow:ellipsis;color:#333238}@media (min-width: 768px){.page-with-contextual-sidebar{padding-left:56px}}@media (min-width: 1200px){.page-with-contextual-sidebar{padding-left:256px}}@media (min-width: 768px){.page-with-icon-sidebar{padding-left:56px}}.nav-sidebar{position:fixed;bottom:0;left:0;z-index:600;width:256px;top:var(--header-height, 48px);background-color:#fbfafd;border-right:1px solid #e9e9e9;transform:translate3d(0, 0, 0)}.nav-sidebar.sidebar-collapsed-desktop{width:56px}.nav-sidebar.sidebar-collapsed-desktop .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar.sidebar-collapsed-desktop .badge.badge-pill:not(.fly-out-badge),.nav-sidebar.sidebar-collapsed-desktop .nav-item-name,.nav-sidebar.sidebar-collapsed-desktop .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar.sidebar-collapsed-desktop .sidebar-top-level-items>li>a{min-height:unset}.nav-sidebar.sidebar-collapsed-desktop .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar.sidebar-collapsed-desktop .avatar-container{margin:0 auto}.nav-sidebar.sidebar-collapsed-desktop li.active:not(.fly-out-top-item)>a{background-color:rgba(41,41,97,0.08)}.nav-sidebar a{text-decoration:none;color:#333238}.nav-sidebar li{white-space:nowrap}.nav-sidebar li .nav-item-name{flex:1;overflow:hidden;text-overflow:ellipsis}.nav-sidebar li>a,.nav-sidebar li>.fly-out-top-item-container{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 8px}.nav-sidebar li.active>a{font-weight:600}.nav-sidebar li.active:not(.fly-out-top-item)>a:not(.has-sub-items){background-color:rgba(0,0,0,0.08)}.nav-sidebar ul{padding-left:0;list-style:none}@media (max-width: 767.98px){.nav-sidebar{left:-256px}}.nav-sidebar .nav-icon-container{display:flex;margin-right:8px}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:-0.25rem;margin-bottom:-0.25rem;margin-top:0;position:relative;color:#fff;background:var(--black, #000)}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container strong{font-weight:400}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container::before{position:absolute;content:"";display:block;top:50%;left:-0.25rem;margin-top:-0.25rem;width:0;height:0;border-top:0.25rem solid transparent;border-bottom:0.25rem solid transparent;border-right:0.25rem solid #000;border-right-color:var(--black, #000)}@media (min-width: 576px){.nav-sidebar a.has-sub-items+.sidebar-sub-level-items{min-width:150px}}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:0;border-bottom-left-radius:0;border-bottom-right-radius:0}@media (min-width: 768px) and (max-width: 1199px){.nav-sidebar:not(.sidebar-expanded-mobile){width:56px}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar:not(.sidebar-expanded-mobile) .badge.badge-pill:not(.fly-out-badge),.nav-sidebar:not(.sidebar-expanded-mobile) .nav-item-name,.nav-sidebar:not(.sidebar-expanded-mobile) .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items>li>a{min-height:unset}.nav-sidebar:not(.sidebar-expanded-mobile) .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar:not(.sidebar-expanded-mobile) .avatar-container{margin:0 auto}.nav-sidebar:not(.sidebar-expanded-mobile) li.active:not(.fly-out-top-item)>a{background-color:rgba(41,41,97,0.08)}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:60px;width:56px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:10px 4px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:auto}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:0.25rem}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items>li .sidebar-sub-level-items:not(.flyout-list){display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-icon-container{margin-right:0}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button{width:55px;padding:0 21px}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .collapse-text{display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}}.nav-sidebar-inner-scroll{height:100%;width:100%;overflow-x:hidden;overflow-y:auto}.nav-sidebar-inner-scroll>div.context-header{margin-top:0.25rem}.nav-sidebar-inner-scroll>div.context-header a{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 8px;padding:0.25rem;margin-bottom:0.25rem;margin-top:0.125rem}.nav-sidebar-inner-scroll>div.context-header a .avatar-container{font-weight:400;flex:none}.sidebar-top-level-items{margin-bottom:60px}.sidebar-top-level-items .context-header a{padding:0.25rem;margin-bottom:0.25rem;margin-top:0.125rem}.sidebar-top-level-items .context-header a .avatar-container{font-weight:400;flex:none}.sidebar-top-level-items>li.active .sidebar-sub-level-items:not(.is-fly-out-only){display:block}.sidebar-top-level-items li>a.gl-link{color:#333238}.sidebar-top-level-items li>a.gl-link:active{text-decoration:none}.sidebar-sub-level-items{padding-top:0;padding-bottom:0;display:none}.sidebar-sub-level-items:not(.fly-out-list) li>a{padding-left:2.25rem}.toggle-sidebar-button,.close-nav-button{height:48px;padding:0 16px;background-color:#fbfafd;border:0;color:#737278;display:flex;align-items:center;background-color:#fbfafd;position:fixed;bottom:0;width:255px}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left,.close-nav-button .collapse-text,.close-nav-button .icon-chevron-double-lg-left{color:inherit}.collapse-text{white-space:nowrap;overflow:hidden}.sidebar-collapsed-desktop .context-header{height:60px;width:56px}.sidebar-collapsed-desktop .context-header a{padding:10px 4px}.sidebar-collapsed-desktop .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.sidebar-collapsed-desktop .context-header{height:auto}.sidebar-collapsed-desktop .context-header a{padding:0.25rem}.sidebar-collapsed-desktop .sidebar-top-level-items>li .sidebar-sub-level-items:not(.flyout-list){display:none}.sidebar-collapsed-desktop .nav-icon-container{margin-right:0}.sidebar-collapsed-desktop .toggle-sidebar-button{width:55px;padding:0 21px}.sidebar-collapsed-desktop .toggle-sidebar-button .collapse-text{display:none}.sidebar-collapsed-desktop .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}.close-nav-button{display:none}@media (max-width: 767.98px){.close-nav-button{display:flex}.toggle-sidebar-button{display:none}}input::-moz-placeholder{color:#89888d;opacity:1}input::-ms-input-placeholder{color:#89888d}input:-ms-input-placeholder{color:#89888d}svg{fill:currentColor}svg.s12{width:12px;height:12px}svg.s16{width:16px;height:16px}svg.s32{width:32px;height:32px}svg.s12{vertical-align:-1px}svg.s16{vertical-align:-3px}.header-content .header-search-new{max-width:640px}.header-search{min-width:320px}@media (min-width: 768px) and (max-width: 1199.98px){.header-search{min-width:200px}}.header-search .keyboard-shortcut-helper{transform:translateY(calc(50% - 2px));box-shadow:none;border-color:transparent}.search{margin:0 8px}.search form{display:block;margin:0;padding:4px;width:200px;line-height:24px;height:32px;border:0;border-radius:4px}@media (min-width: 1200px){.search form{width:320px}}.search .search-input{border:0;font-size:14px;padding:0 20px 0 0;margin-left:5px;line-height:25px;width:98%;color:#fff;background:none}.search .search-input-container{display:flex;position:relative}.search .search-input-wrap{width:100%}.search .search-input-wrap .search-icon,.search .search-input-wrap .clear-icon{position:absolute;right:5px;top:4px}.search .search-input-wrap .search-icon{-webkit-user-select:none;user-select:none}.search .search-input-wrap .clear-icon{display:none}.search .search-input-wrap .dropdown{position:static}.search .search-input-wrap .dropdown-menu{left:-5px;max-height:400px;overflow:auto}@media (min-width: 1200px){.search .search-input-wrap .dropdown-menu{width:320px}}.search .identicon{flex-basis:16px;flex-shrink:0;margin-right:4px}.avatar,.avatar-container{float:left;margin-right:16px;border-radius:50%}.avatar.s16,.avatar-container.s16{width:16px;height:16px;margin-right:8px}.avatar.s32,.avatar-container.s32{width:32px;height:32px;margin-right:8px}.avatar{transition-property:none;width:40px;height:40px;padding:0;background:#fefefe;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(31,30,36,0.1)}.avatar.avatar-tile{border-radius:0;border:0}.identicon{text-align:center;vertical-align:top;color:#333238;background-color:#ececef}.identicon.s16{font-size:10px;line-height:16px}.identicon.s32{font-size:14px;line-height:32px}.identicon.bg1{background-color:#fcf1ef}.identicon.bg2{background-color:#f4f0ff}.identicon.bg3{background-color:#f1f1ff}.identicon.bg4{background-color:#e9f3fc}.identicon.bg5{background-color:#ecf4ee}.identicon.bg6{background-color:#fdf1dd}.identicon.bg7{background-color:#ececef}.avatar-container{overflow:hidden;display:flex}.avatar-container a{width:100%;height:100%;display:flex;text-decoration:none}.avatar-container .avatar{border-radius:0;border:0;height:auto;width:100%;margin:0;align-self:center}.rect-avatar{border-radius:2px}.rect-avatar.s16{border-radius:2px}.rect-avatar.s16 .avatar{border-radius:2px}.rect-avatar.s32{border-radius:4px}.rect-avatar.s32 .avatar{border-radius:4px}.tab-width-8{tab-size:8}.gl-sr-only{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.gl-border-none\!{border-style:none !important}.gl-display-none{display:none}@media (min-width: 576px){.gl-sm-display-none{display:none}}.gl-display-flex{display:flex}@media (min-width: 992px){.gl-lg-display-flex{display:flex}}@media (min-width: 576px){.gl-sm-display-block{display:block}}@media (min-width: 992px){.gl-lg-display-block{display:block}}.gl-align-items-center{align-items:center}.gl-align-items-stretch{align-items:stretch}.gl-flex-grow-1{flex-grow:1}.gl-justify-content-end{justify-content:flex-end}.gl-relative{position:relative}.gl-absolute{position:absolute}.gl-top-0{top:0}.gl-right-3{right:0.5rem}.gl-w-full{width:100%}.gl-px-3{padding-left:0.5rem;padding-right:0.5rem}.gl-pr-2{padding-right:0.25rem}.gl-pt-0{padding-top:0}.gl-mr-auto{margin-right:auto}.gl-mr-3{margin-right:0.5rem}.gl-ml-n2{margin-left:-0.25rem}.gl-ml-3{margin-left:0.5rem}.gl-mx-0\!{margin-left:0 !important;margin-right:0 !important}.gl-text-right{text-align:right}.gl-white-space-nowrap{white-space:nowrap}.gl-font-sm{font-size:0.75rem}.gl-font-weight-bold{font-weight:600}.gl-z-index-1{z-index:1}.cloak-startup,.content-wrapper>.alert-wrapper,#content-body,.modal-dialog{display:none}

</style>


<link rel="stylesheet" media="all" href="./README_files/application-7ac3b54e2ee2a129462d6702c9857a04f1a405f7254b89a2b3dfc7e73e80a489.css" data-startupcss="loaded">
<link rel="stylesheet" media="all" href="./README_files/editor-f840dc4410cbb2ae0e7da3cbbe6f20f3073e3fe4ca3b99215d97fa8b71d50ec6.css" data-startupcss="loaded">
<link rel="stylesheet" media="all" href="./README_files/application_utilities-6e21d68b1ca9da299256cfb26f7422439a6d11822c228fc18238d1c7d737f1df.css" data-startupcss="loaded">


<link rel="stylesheet" media="all" href="./README_files/white-925931f55f1eb5f0fdef8460d44b95748a47b6d0ecf3e9a50587f3686ff7c5bd.css" data-startupcss="loaded">
<script async="" src="./README_files/sp-bc5b4b4067898d2d20c35fec045d91d032cb739c3deab5f42607edbeca08323a.js"></script><script nonce="">
//<![CDATA[
document.querySelectorAll('link[media="print"]').forEach(linkTag => {
  linkTag.setAttribute('data-startupcss', 'loading');
  const startupLinkLoadedEvent = new CustomEvent('CSSStartupLinkLoaded');
  linkTag.addEventListener('load',function(){this.media='all';this.setAttribute('data-startupcss', 'loaded');document.dispatchEvent(startupLinkLoadedEvent);},{once: true});
})

//]]>
</script>

<script nonce="">
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://gitlab.com/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.user_color_scheme="white";gon.markdown_surround_selection=true;gon.markdown_automatic_lists=true;gon.sentry_dsn="https://526a2f38a53d44e3a8e69bfa001d1e8b@sentry.gitlab.net/15";gon.sentry_environment="gprd";gon.recaptcha_api_server_url="https://www.google.com/recaptcha/api.js";gon.recaptcha_sitekey="6LfAERQTAAAAAL4GYSiAMGLbcLyUIBSfPrDNJgeC";gon.gitlab_url="https://gitlab.com";gon.revision="88ae73996f6";gon.feature_category="source_code_management";gon.gitlab_logo="/assets/gitlab_logo-2957169c8ef64c58616a1ac3f4fc626e8a35ce4eb3ed31bb0d873712f2a041a0.png";gon.secure=true;gon.sprite_icons="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg";gon.sprite_file_icons="/assets/file_icons-958d18a1c33aa82a81e2eb1ffbffc33131d501c41ad95838a70b089e5ffbd7a0.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-e1b1ba2d7a86a445dcb1110d1b6e7dd0200ecaa993a445df77a07537dbf8f475.css";gon.select2_css_path="/assets/lazy_bundles/select2-f3964bfc05fa591b32f66a871083754d3a3161c3c5a63a0a45449cb651d3416a.css";gon.gridstack_css_path="/assets/lazy_bundles/gridstack-f9e005145f1f29d3fd436ec6eda8b264c017ee47886472841ed47e32332518ff.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#009966":"Green-cyan","#8fbc8f":"Dark sea green","#3cb371":"Medium sea green","#00b140":"Green screen","#013220":"Dark green","#6699cc":"Blue-gray","#0000ff":"Blue","#e6e6fa":"Lavender","#9400d3":"Dark violet","#330066":"Deep violet","#808080":"Gray","#36454f":"Charcoal grey","#f7e7ce":"Champagne","#c21e56":"Rose red","#cc338b":"Magenta-pink","#dc143c":"Crimson","#ff0000":"Red","#cd5b45":"Dark coral","#eee600":"Titanium yellow","#ed9121":"Carrot orange","#c39953":"Aztec Gold"};gon.first_day_of_week=0;gon.time_display_relative=true;gon.ee=true;gon.jh=false;gon.dot_com=true;gon.current_user_id=12959903;gon.current_username="md_manish";gon.current_user_fullname="Md Manishurrahman";gon.current_user_avatar_url="https://secure.gravatar.com/avatar/339a5a437f934e7f4f79a776a044609a?s=80\u0026d=identicon";gon.features={"usageDataApi":true,"securityAutoFix":false,"newHeaderSearch":true,"sourceEditorToolbar":false,"integrationSlackAppNotifications":false,"vueGroupSelect":false,"highlightJs":true,"fileLineBlame":false};gon.roadmap_epics_limit=1000;gon.subscriptions_url="https://customers.gitlab.com";gon.payment_form_url="https://customers.gitlab.com/payment_forms/cc_validation";gon.payment_validation_form_id="payment_method_validation";gon.registration_validation_form_url="https://customers.gitlab.com/payment_forms/cc_registration_validation";
//]]>
</script>


<script src="./README_files/runtime.6c092ae1.bundle.js" defer="defer" nonce=""></script>
<script src="./README_files/main.11d63fc6.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/sentry.55fae27a.chunk.js" defer="defer" nonce=""></script>


<script src="./README_files/graphql.7a7c3f9d.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/3.af087be4.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/shortcutsBundle.82128b61.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/5.ab694314.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/commons-pages.groups.boards-pages.groups.details-pages.groups.epic_boards-pages.groups.show-pages.gr-e98a9328.79d008ae.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-24befec6.7e3dfd45.chunk.js" defer="defer" nonce=""></script>
<script src="./README_files/pages.projects.blob.edit.5a554d66.chunk.js" defer="defer" nonce=""></script>
<script nonce="">
//<![CDATA[
window.uploads_path = "/mountblue/cohort-22-python/manish/ipl-data-set-analytics/uploads";



//]]>
</script>
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="Edit · README.md · main · mountblue / Cohort 22 Python / Manish / IPL data set analytics · GitLab" property="og:title">
<meta content="GitLab.com" property="og:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="Edit · README.md · main · mountblue / Cohort 22 Python / Manish / IPL data set analytics · GitLab" property="twitter:title">
<meta content="GitLab.com" property="twitter:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta content="GitLab.com" name="description">
<link href="https://gitlab.com/-/manifest.json" rel="manifest">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#292961" name="theme-color">
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="wGbTQphua50gRAKxVixGmSHRPBC7y9DXD8p0Zwrr+AyS4AUP2CoTDvPJlUHtLwaVOoaailstmetpEFeltNctpQ==">
<meta name="csp-nonce" content="3UmblWv9ICX6p8Fi0pHdQQ==">
<meta name="action-cable-url" content="/-/cable">
<link rel="apple-touch-icon" type="image/x-icon" href="https://gitlab.com/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png">
<link href="https://gitlab.com/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">



<script nonce="">
//<![CDATA[
;(function(p,l,o,w,i,n,g){if(!p[i]){p.GlobalSnowplowNamespace=p.GlobalSnowplowNamespace||[];
p.GlobalSnowplowNamespace.push(i);p[i]=function(){(p[i].q=p[i].q||[]).push(arguments)
};p[i].q=p[i].q||[];n=l.createElement(o);g=l.getElementsByTagName(o)[0];n.async=1;
n.src=w;g.parentNode.insertBefore(n,g)}}(window,document,"script","https://gitlab.com/assets/snowplow/sp-bc5b4b4067898d2d20c35fec045d91d032cb739c3deab5f42607edbeca08323a.js","snowplow"));

window.snowplowOptions = {"namespace":"gl","hostname":"snowplow.trx.gitlab.net","cookieDomain":".gitlab.com","appId":"gitlab","formTracking":true,"linkClickTracking":true}

gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-0-8","data":{"environment":"production","source":"gitlab-rails","plan":"free","extra":{},"user_id":12959903,"namespace_id":60082598,"project_id":40954144,"context_generated_at":"2022-11-20T18:05:12.606Z"}}
gl.snowplowPseudonymizedPageUrl = "https://gitlab.com/namespace60082598/project40954144/-/edit/:repository_path";


//]]>
</script>

<script charset="utf-8" src="./README_files/hello.288f5b48.chunk.js"></script><script charset="utf-8" src="./README_files/monaco.a6d661ed.chunk.js"></script><script charset="utf-8" src="./README_files/78.542a0900.chunk.js"></script><script charset="utf-8" src="./README_files/88.07b28fcd.chunk.js"></script><script charset="utf-8" src="./README_files/959.e24b6908.chunk.js"></script><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .accessibilityHelpWidget {
	padding: 10px;
	vertical-align: middle;
	overflow: scroll;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-aria-container {
	position: absolute; /* try to hide from window but not from screen readers */
	left:-999em;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .selection-anchor {
	background-color: #007ACC;
	width: 2px !important;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .bracket-match {
	box-sizing: border-box;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .monaco-editor-overlaymessage {
	padding-bottom: 8px;
	z-index: 10000;
}

.monaco-editor .monaco-editor-overlaymessage.below {
	padding-bottom: 0;
	padding-top: 8px;
	z-index: 10000;
}

@keyframes fadeIn {
	from { opacity: 0; }
	to { opacity: 1; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeIn {
	animation: fadeIn 150ms ease-out;
}

@keyframes fadeOut {
	from { opacity: 1; }
	to { opacity: 0; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeOut {
	animation: fadeOut 100ms ease-out;
}

.monaco-editor .monaco-editor-overlaymessage .message {
	padding: 1px 4px;
}

.monaco-editor .monaco-editor-overlaymessage .anchor {
	width: 0 !important;
	height: 0 !important;
	border-color: transparent;
	border-style: solid;
	z-index: 1000;
	border-width: 8px;
	position: absolute;
}

.monaco-editor .monaco-editor-overlaymessage:not(.below) .anchor.top,
.monaco-editor .monaco-editor-overlaymessage.below .anchor.below {
	display: none;
}

.monaco-editor .monaco-editor-overlaymessage.below .anchor.top {
	display: inherit;
	top: -8px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .contentWidgets .codicon-light-bulb,
.monaco-editor .contentWidgets .codicon-lightbulb-autofix {
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-editor .contentWidgets .codicon-light-bulb:hover,
.monaco-editor .contentWidgets .codicon-lightbulb-autofix:hover {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .codelens-decoration {
	overflow: hidden;
	display: inline-block;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .codelens-decoration > span,
.monaco-editor .codelens-decoration > a {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	white-space: nowrap;
	vertical-align: sub;
}

.monaco-editor .codelens-decoration > a {
	text-decoration: none;
}

.monaco-editor .codelens-decoration > a:hover {
	cursor: pointer;
}

.monaco-editor .codelens-decoration .codicon {
	vertical-align: middle;
	color: currentColor !important;
}

.monaco-editor .codelens-decoration > a:hover .codicon::before {
	cursor: pointer;
}

@keyframes fadein {
	0% { opacity: 0; visibility: visible;}
	100% { opacity: 1; }
}

.monaco-editor .codelens-decoration.fadein {
	animation: fadein 0.1s linear;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .goto-definition-link {
	text-decoration: underline;
	cursor: pointer;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar {
	white-space: nowrap;
	height: 100%;
}

.monaco-action-bar .actions-container {
	display: flex;
	margin: 0 auto;
	padding: 0;
	height: 100%;
	width: 100%;
	align-items: center;
}

.monaco-action-bar.vertical .actions-container {
	display: inline-block;
}

.monaco-action-bar .action-item {
	display: block;
	align-items: center;
	justify-content: center;
	cursor: pointer;
	position: relative;  /* DO NOT REMOVE - this is the key to preventing the ghosting icon bug in Chrome 42 */
}

.monaco-action-bar .action-item.disabled {
	cursor: default;
}

.monaco-action-bar .action-item .icon,
.monaco-action-bar .action-item .codicon {
	display: block;
}

.monaco-action-bar .action-item .codicon {
	display: flex;
	align-items: center;
	width: 16px;
	height: 16px;
}

.monaco-action-bar .action-label {
	font-size: 11px;
	padding: 3px;
	border-radius: 5px;
}

.monaco-action-bar .action-item.disabled .action-label,
.monaco-action-bar .action-item.disabled .action-label::before,
.monaco-action-bar .action-item.disabled .action-label:hover {
	opacity: 0.4;
}

/* Vertical actions */

.monaco-action-bar.vertical {
	text-align: left;
}

.monaco-action-bar.vertical .action-item {
	display: block;
}

.monaco-action-bar.vertical .action-label.separator {
	display: block;
	border-bottom: 1px solid #bbb;
	padding-top: 1px;
	margin-left: .8em;
	margin-right: .8em;
}

.monaco-action-bar .action-item .action-label.separator {
	width: 1px;
	height: 16px;
	margin: 5px 4px !important;
	cursor: default;
	min-width: 1px;
	padding: 0;
	background-color: #bbb;
}

.secondary-actions .monaco-action-bar .action-label {
	margin-left: 6px;
}

/* Action Items */
.monaco-action-bar .action-item.select-container {
	overflow: hidden; /* somehow the dropdown overflows its container, we prevent it here to not push */
	flex: 1;
	max-width: 170px;
	min-width: 60px;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: 10px;
}

.monaco-action-bar .action-item.action-dropdown-item {
	display: flex;
}

.monaco-action-bar .action-item.action-dropdown-item > .action-label {
	margin-right: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .peekview-widget .head {
	box-sizing: border-box;
	display: flex;
}

.monaco-editor .peekview-widget .head .peekview-title {
	display: flex;
	align-items: center;
	font-size: 13px;
	margin-left: 20px;
	min-width: 0;
}

.monaco-editor .peekview-widget .head .peekview-title.clickable {
	cursor: pointer;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname:not(:empty) {
	font-size: 0.9em;
	margin-left: 0.5em;
}

.monaco-editor .peekview-widget .head .peekview-title .meta {
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname {
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .filename {
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .meta:not(:empty)::before {
	content: '-';
	padding: 0 0.3em;
}

.monaco-editor .peekview-widget .head .peekview-actions {
	flex: 1;
	text-align: right;
	padding-right: 2px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar {
	display: inline-block;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar,
.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar > .actions-container {
	height: 100%;
}

.monaco-editor .peekview-widget > .body {
	border-top: 1px solid;
	position: relative;
}

.monaco-editor .peekview-widget .head .peekview-title .codicon {
	margin-right: 4px;
}

.monaco-editor .peekview-widget .monaco-list .monaco-list-row.focused .codicon {
	color: inherit !important;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -------------------- IE10 remove auto clear button -------------------- */

::-ms-clear {
	display: none;
}

/* All widgets */
/* I am not a big fan of this rule */
.monaco-editor .editor-widget input {
	color: inherit;
}

/* -------------------- Editor -------------------- */

.monaco-editor {
	position: relative;
	overflow: visible;
	-webkit-text-size-adjust: 100%;
}

/* -------------------- Misc -------------------- */

.monaco-editor .overflow-guard {
	position: relative;
	overflow: hidden;
}

.monaco-editor .view-overlays {
	position: absolute;
	top: 0;
}

/*
.monaco-editor .auto-closed-character {
	opacity: 0.3;
}
*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .inputarea {
	min-width: 0;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	outline: none !important;
	resize: none;
	border: none;
	overflow: hidden;
	color: transparent;
	background-color: transparent;
}
/*.monaco-editor .inputarea {
	position: fixed !important;
	width: 800px !important;
	height: 500px !important;
	top: initial !important;
	left: initial !important;
	bottom: 0 !important;
	right: 0 !important;
	color: black !important;
	background: white !important;
	line-height: 15px !important;
	font-size: 14px !important;
}*/
.monaco-editor .inputarea.ime-input {
	z-index: 10;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .line-numbers {
	font-variant-numeric: tabular-nums;
	position: absolute;
	text-align: right;
	display: inline-block;
	vertical-align: middle;
	box-sizing: border-box;
	cursor: default;
	height: 100%;
}

.monaco-editor .relative-current-line-number {
	text-align: left;
	display: inline-block;
	width: 100%;
}

.monaco-editor .margin-view-overlays .line-numbers.lh-odd {
	margin-top: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-mouse-cursor-text {
	cursor: text;
}

/* The following selector looks a bit funny, but that is needed to cover all the workbench and the editor!! */
.vs-dark .mac .monaco-mouse-cursor-text, .hc-black .mac .monaco-mouse-cursor-text,
.vs-dark.mac .monaco-mouse-cursor-text, .hc-black.mac .monaco-mouse-cursor-text {
	cursor: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAAL0lEQVQoz2NgCD3x//9/BhBYBWdhgFVAiVW4JBFKGIa4AqD0//9D3pt4I4tAdAMAHTQ/j5Zom30AAAAASUVORK5CYII=) 1x, url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAz0lEQVRIx2NgYGBY/R8I/vx5eelX3n82IJ9FxGf6tksvf/8FiTMQAcAGQMDvSwu09abffY8QYSAScNk45G198eX//yev73/4///701eh//kZSARckrNBRvz//+8+6ZohwCzjGNjdgQxkAg7B9WADeBjIBqtJCbhRA0YNoIkBSNmaPEMoNmA0FkYNoFKhapJ6FGyAH3nauaSmPfwI0v/3OukVi0CIZ+F25KrtYcx/CTIy0e+rC7R1Z4KMICVTQQ14feVXIbR695u14+Ir4gwAAD49E54wc1kWAAAAAElFTkSuQmCC) 2x) 5 8, text;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line.current-line-margin.current-line-margin-both {
	border-right: 0;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cdr = core decorations rendering (div)
*/
.monaco-editor .lines-content .cdr {
	position: absolute;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Arrows */
.monaco-scrollable-element > .scrollbar > .scra {
	cursor: pointer;
	font-size: 11px !important;
}

.monaco-scrollable-element > .visible {
	opacity: 1;

	/* Background rule added for IE9 - to allow clicks on dom node */
	background:rgba(0,0,0,0);

	transition: opacity 100ms linear;
}
.monaco-scrollable-element > .invisible {
	opacity: 0;
	pointer-events: none;
}
.monaco-scrollable-element > .invisible.fade {
	transition: opacity 800ms linear;
}

/* Scrollable Content Inset Shadow */
.monaco-scrollable-element > .shadow {
	position: absolute;
	display: none;
}
.monaco-scrollable-element > .shadow.top {
	display: block;
	top: 0;
	left: 3px;
	height: 3px;
	width: 100%;
}
.monaco-scrollable-element > .shadow.left {
	display: block;
	top: 3px;
	left: 0;
	height: 100%;
	width: 3px;
}
.monaco-scrollable-element > .shadow.top-left-corner {
	display: block;
	top: 0;
	left: 0;
	height: 3px;
	width: 3px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .glyph-margin {
	position: absolute;
	top: 0;
}

/*
	Keeping name short for faster parsing.
	cgmr = core glyph margin rendering (div)
*/
.monaco-editor .margin-view-overlays .cgmr {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .lines-content .core-guide {
	position: absolute;
	box-sizing: border-box;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Uncomment to see lines flashing when they're painted */
/*.monaco-editor .view-lines > .view-line {
	background-color: none;
	animation-name: flash-background;
	animation-duration: 800ms;
}
@keyframes flash-background {
	0%   { background-color: lightgreen; }
	100% { background-color: none }
}*/

.mtkcontrol {
	color: rgb(255, 255, 255) !important;
	background: rgb(150, 0, 0) !important;
}

.monaco-editor.no-user-select .lines-content,
.monaco-editor.no-user-select .view-line,
.monaco-editor.no-user-select .view-lines {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .view-lines {
	white-space: nowrap;
}

.monaco-editor .view-line {
	position: absolute;
	width: 100%;
}

.monaco-editor .mtkz {
	display: inline-block;
}

/* TODO@tokenization bootstrap fix */
/*.monaco-editor .view-line > span > span {
	float: none;
	min-height: inherit;
	margin-left: inherit;
}*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .lines-decorations {
	position: absolute;
	top: 0;
	background: white;
}

/*
	Keeping name short for faster parsing.
	cldr = core lines decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cldr {
	position: absolute;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cmdr = core margin decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cmdr {
	position: absolute;
	left: 0;
	width: 100%;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* START cover the case that slider is visible on mouseover */
.monaco-editor .minimap.slider-mouseover .minimap-slider {
	opacity: 0;
	transition: opacity 100ms linear;
}
.monaco-editor .minimap.slider-mouseover:hover .minimap-slider {
	opacity: 1;
}
.monaco-editor .minimap.slider-mouseover .minimap-slider.active {
	opacity: 1;
}
/* END cover the case that slider is visible on mouseover */

.monaco-editor .minimap-shadow-hidden {
	position: absolute;
	width: 0;
}
.monaco-editor .minimap-shadow-visible {
	position: absolute;
	left: -6px;
	width: 6px;
}
.monaco-editor.no-minimap-shadow .minimap-shadow-visible {
	position: absolute;
	left: -1px;
	width: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .overlayWidgets {
	position: absolute;
	top: 0;
	left:0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-ruler {
	position: absolute;
	top: 0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .scroll-decoration {
	position: absolute;
	top: 0;
	left: 0;
	height: 6px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cslr = core selections layer rendering (div)
*/
.monaco-editor .lines-content .cslr {
	position: absolute;
}

.monaco-editor			.top-left-radius		{ border-top-left-radius: 3px; }
.monaco-editor			.bottom-left-radius		{ border-bottom-left-radius: 3px; }
.monaco-editor			.top-right-radius		{ border-top-right-radius: 3px; }
.monaco-editor			.bottom-right-radius	{ border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-black .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-black .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-black .bottom-right-radius	{ border-bottom-right-radius: 0; }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .cursors-layer {
	position: absolute;
	top: 0;
}

.monaco-editor .cursors-layer > .cursor {
	position: absolute;
	overflow: hidden;
}

/* -- smooth-caret-animation -- */
.monaco-editor .cursors-layer.cursor-smooth-caret-animation > .cursor {
	transition: all 80ms;
}

/* -- block-outline-style -- */
.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor {
	box-sizing: border-box;
	background: transparent !important;
	border-style: solid;
	border-width: 1px;
}

/* -- underline-style -- */
.monaco-editor .cursors-layer.cursor-underline-style > .cursor {
	border-bottom-width: 2px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

/* -- underline-thin-style -- */
.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

@keyframes monaco-cursor-smooth {
	0%,
	20% {
		opacity: 1;
	}
	60%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-phase {
	0%,
	20% {
		opacity: 1;
	}
	90%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-expand {
	0%,
	20% {
		transform: scaleY(1);
	}
	80%,
	100% {
		transform: scaleY(0);
	}
}

.cursor-smooth {
	animation: monaco-cursor-smooth 0.5s ease-in-out 0s 20 alternate;
}

.cursor-phase {
	animation: monaco-cursor-phase 0.5s ease-in-out 0s 20 alternate;
}

.cursor-expand > .cursor {
	animation: monaco-cursor-expand 0.5s ease-in-out 0s 20 alternate;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

:root {
	--sash-size: 4px;
}

.monaco-sash {
	position: absolute;
	z-index: 35;
	touch-action: none;
}

.monaco-sash.disabled {
	pointer-events: none;
}

.monaco-sash.mac.vertical {
	cursor: col-resize;
}

.monaco-sash.vertical.minimum {
	cursor: e-resize;
}

.monaco-sash.vertical.maximum {
	cursor: w-resize;
}

.monaco-sash.mac.horizontal {
	cursor: row-resize;
}

.monaco-sash.horizontal.minimum {
	cursor: s-resize;
}

.monaco-sash.horizontal.maximum {
	cursor: n-resize;
}

.monaco-sash.disabled {
	cursor: default !important;
	pointer-events: none !important;
}

.monaco-sash.vertical {
	cursor: ew-resize;
	top: 0;
	width: var(--sash-size);
	height: 100%;
}

.monaco-sash.horizontal {
	cursor: ns-resize;
	left: 0;
	width: 100%;
	height: var(--sash-size);
}

.monaco-sash:not(.disabled) > .orthogonal-drag-handle {
	content: " ";
	height: calc(var(--sash-size) * 2);
	width: calc(var(--sash-size) * 2);
	z-index: 100;
	display: block;
	cursor: all-scroll;
	position: absolute;
}

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled)
	> .orthogonal-drag-handle.start,
.monaco-sash.horizontal.orthogonal-edge-south:not(.disabled)
	> .orthogonal-drag-handle.end {
	cursor: nwse-resize;
}

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled)
	> .orthogonal-drag-handle.end,
.monaco-sash.horizontal.orthogonal-edge-south:not(.disabled)
	> .orthogonal-drag-handle.start {
	cursor: nesw-resize;
}

.monaco-sash.vertical > .orthogonal-drag-handle.start {
	left: calc(var(--sash-size) * -0.5);
	top: calc(var(--sash-size) * -1);
}
.monaco-sash.vertical > .orthogonal-drag-handle.end {
	left: calc(var(--sash-size) * -0.5);
	bottom: calc(var(--sash-size) * -1);
}
.monaco-sash.horizontal > .orthogonal-drag-handle.start {
	top: calc(var(--sash-size) * -0.5);
	left: calc(var(--sash-size) * -1);
}
.monaco-sash.horizontal > .orthogonal-drag-handle.end {
	top: calc(var(--sash-size) * -0.5);
	right: calc(var(--sash-size) * -1);
}

.monaco-sash:before {
	content: '';
	pointer-events: none;
	position: absolute;
	width: 100%;
	height: 100%;
	transition: background-color 0.1s ease-out;
	background: transparent;
}

.monaco-sash.vertical:before {
	width: var(--sash-hover-size);
	left: calc(50% - (var(--sash-hover-size) / 2));
}

.monaco-sash.horizontal:before {
	height: var(--sash-hover-size);
	top: calc(50% - (var(--sash-hover-size) / 2));
}

/** Debug **/

.monaco-sash.debug {
	background: cyan;
}

.monaco-sash.debug.disabled {
	background: rgba(0, 255, 255, 0.2);
}

.monaco-sash.debug:not(.disabled) > .orthogonal-drag-handle {
	background: red;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .zone-widget {
	position: absolute;
	z-index: 10;
}


.monaco-editor .zone-widget .zone-widget-container {
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-width: 0;
	border-bottom-width: 0;
	position: relative;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-dropdown {
	height: 100%;
	padding: 0;
}

.monaco-dropdown > .dropdown-label {
	cursor: pointer;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-dropdown > .dropdown-label > .action-label.disabled {
	cursor: default;
}

.monaco-dropdown-with-primary {
	display: flex !important;
	flex-direction: row;
	border-radius: 5px;
}

.monaco-dropdown-with-primary > .action-container > .action-label {
	margin-right: 0;
}

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdown > .dropdown-label .codicon[class*='codicon-'] {
	font-size: 12px;
	padding-left: 0px;
	padding-right: 0px;
	line-height: 16px;
	margin-left: -3px;
}

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdown > .dropdown-label > .action-label {
	display: block;
	background-size: 16px;
	background-position: center center;
	background-repeat: no-repeat;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar .action-item.menu-entry .action-label.icon {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	background-position: 50%;
	background-size: 16px;
}

.monaco-action-bar .action-item.menu-entry .action-label {
	background-image: var(--menu-entry-icon-light);
}

.vs-dark .monaco-action-bar .action-item.menu-entry .action-label,
.hc-black .monaco-action-bar .action-item.menu-entry .action-label {
	background-image: var(--menu-entry-icon-dark);
}


.monaco-dropdown-with-default {
	display: flex !important;
	flex-direction: row;
	border-radius: 5px;
}

.monaco-dropdown-with-default > .action-container > .action-label {
	margin-right: 0;
}

.monaco-dropdown-with-default > .action-container.menu-entry > .action-label.icon {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	background-position: 50%;
	background-size: 16px;
}

.monaco-dropdown-with-default > .action-container.menu-entry > .action-label {
	background-image: var(--menu-entry-icon-light);
}

.vs-dark .monaco-dropdown-with-default > .action-container.menu-entry > .action-label,
.hc-black .monaco-dropdown-with-default > .action-container.menu-entry > .action-label {
	background-image: var(--menu-entry-icon-dark);
}

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdown > .dropdown-label .codicon[class*='codicon-'] {
	font-size: 12px;
	padding-left: 0px;
	padding-right: 0px;
	line-height: 16px;
	margin-left: -3px;
}

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdown > .dropdown-label > .action-label {
	display: block;
	background-size: 16px;
	background-position: center center;
	background-repeat: no-repeat;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list {
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-list.mouse-support {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-list > .monaco-scrollable-element {
	height: 100%;
}

.monaco-list-rows {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-list.horizontal-scrolling .monaco-list-rows {
	width: auto;
	min-width: 100%;
}

.monaco-list-row {
	position: absolute;
	box-sizing: border-box;
	overflow: hidden;
	width: 100%;
}

.monaco-list.mouse-support .monaco-list-row {
	cursor: pointer;
	touch-action: none;
}

/* for OS X ballistic scrolling */
.monaco-list-row.scrolling {
	display: none !important;
}

/* Focus */
.monaco-list.element-focused,
.monaco-list.selection-single,
.monaco-list.selection-multiple {
	outline: 0 !important;
}

/* Dnd */
.monaco-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
	z-index: 1000;
}

/* Type filter */

.monaco-list-type-filter {
	display: flex;
	align-items: center;
	position: absolute;
	border-radius: 2px;
	padding: 0px 3px;
	max-width: calc(100% - 10px);
	text-overflow: ellipsis;
	overflow: hidden;
	text-align: right;
	box-sizing: border-box;
	cursor: all-scroll;
	font-size: 13px;
	line-height: 18px;
	height: 20px;
	z-index: 1;
	top: 4px;
}

.monaco-list-type-filter.dragging {
	transition: top 0.2s, left 0.2s;
}

.monaco-list-type-filter.ne {
	right: 4px;
}

.monaco-list-type-filter.nw {
	left: 4px;
}

.monaco-list-type-filter > .controls {
	display: flex;
	align-items: center;
	box-sizing: border-box;
	transition: width 0.2s;
	width: 0;
}

.monaco-list-type-filter.dragging > .controls,
.monaco-list-type-filter:hover > .controls {
	width: 36px;
}

.monaco-list-type-filter > .controls > * {
	border: none;
	box-sizing: border-box;
	-webkit-appearance: none;
	-moz-appearance: none;
	background: none;
	width: 16px;
	height: 16px;
	flex-shrink: 0;
	margin: 0;
	padding: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}

.monaco-list-type-filter > .controls > .filter {
	margin-left: 4px;
}

.monaco-list-type-filter-message {
	position: absolute;
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	padding: 40px 1em 1em 1em;
	text-align: center;
	white-space: normal;
	opacity: 0.7;
	pointer-events: none;
}

.monaco-list-type-filter-message:empty {
	display: none;
}

/* Electron */

.monaco-list-type-filter {
	cursor: grab;
}

.monaco-list-type-filter.dragging {
	cursor: grabbing;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-split-view2 {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .sash-container {
	position: absolute;
	width: 100%;
	height: 100%;
	pointer-events: none;
}

.monaco-split-view2 > .sash-container > .monaco-sash {
	pointer-events: initial;
}

.monaco-split-view2 > .monaco-scrollable-element {
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container {
	width: 100%;
	height: 100%;
	white-space: nowrap;
	position: relative;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > .split-view-view {
	white-space: initial;
	position: absolute;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > .split-view-view:not(.visible) {
	display: none;
}

.monaco-split-view2.vertical > .monaco-scrollable-element > .split-view-container > .split-view-view {
	width: 100%;
}

.monaco-split-view2.horizontal > .monaco-scrollable-element > .split-view-container > .split-view-view {
	height: 100%;
}

.monaco-split-view2.separator-border > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	content: ' ';
	position: absolute;
	top: 0;
	left: 0;
	z-index: 5;
	pointer-events: none;
	background-color: var(--separator-border);
}

.monaco-split-view2.separator-border.horizontal > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 100%;
	width: 1px;
}

.monaco-split-view2.separator-border.vertical > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 1px;
	width: 100%;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-table {
	display: flex;
	flex-direction: column;
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-table > .monaco-split-view2 {
	border-bottom: 1px solid transparent;
}

.monaco-table > .monaco-list {
	flex: 1;
}

.monaco-table-tr {
	display: flex;
	height: 100%;
}

.monaco-table-th {
	width: 100%;
	height: 100%;
	font-weight: bold;
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-table-th,
.monaco-table-td {
	box-sizing: border-box;
	flex-shrink: 0;
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
}

.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
	content: "";
	position: absolute;
	left: calc(var(--sash-size) / 2);
	width: 0;
	border-left: 1px solid transparent;
}

.monaco-table > .monaco-split-view2,
.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
	transition: border-color 0.2s ease-out;
}
/*
.monaco-table:hover > .monaco-split-view2,
.monaco-table:hover > .monaco-split-view2 .monaco-sash.vertical::before {
	border-color: rgba(204, 204, 204, 0.2);
} */
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-tl-row {
	display: flex;
	height: 100%;
	align-items: center;
	position: relative;
}

.monaco-tl-indent {
	height: 100%;
	position: absolute;
	top: 0;
	left: 16px;
	pointer-events: none;
}

.hide-arrows .monaco-tl-indent {
	left: 12px;
}

.monaco-tl-indent > .indent-guide {
	display: inline-block;
	box-sizing: border-box;
	height: 100%;
	border-left: 1px solid transparent;
}

.monaco-tl-indent > .indent-guide {
	transition: border-color 0.1s linear;
}

.monaco-tl-twistie,
.monaco-tl-contents {
	height: 100%;
}

.monaco-tl-twistie {
	font-size: 10px;
	text-align: right;
	padding-right: 6px;
	flex-shrink: 0;
	width: 16px;
	display: flex !important;
	align-items: center;
	justify-content: center;
	transform: translateX(3px);
}

.monaco-tl-contents {
	flex: 1;
	overflow: hidden;
}

.monaco-tl-twistie::before {
	border-radius: 20px;
}

.monaco-tl-twistie.collapsed::before {
	transform: rotate(-90deg);
}

.monaco-tl-twistie.codicon-tree-item-loading::before {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.25s steps(30) infinite;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -- zone widget */
.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget {
	border-top-width: 1px;
	border-bottom-width: 1px;
}

.monaco-editor .reference-zone-widget .inline {
	display: inline-block;
	vertical-align: top;
}

.monaco-editor .reference-zone-widget .messages {
	height: 100%;
	width: 100%;
	text-align: center;
	padding: 3em 0;
}

.monaco-editor .reference-zone-widget .ref-tree {
	line-height: 23px;
}

.monaco-editor .reference-zone-widget .ref-tree .reference {
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file {
	display: inline-flex;
	width: 100%;
	height: 100%;
}

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .selected .reference-file {
	color: inherit !important;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file .count {
	margin-right: 12px;
	margin-left: auto;
}

/* High Contrast Theming */

.monaco-editor.hc-black .reference-zone-widget .ref-tree .reference-file {
	font-weight: bold;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-count-badge {
	padding: 3px 6px;
	border-radius: 11px;
	font-size: 11px;
	min-width: 18px;
	min-height: 18px;
	line-height: 11px;
	font-weight: normal;
	text-align: center;
	display: inline-block;
	box-sizing: border-box;
}

.monaco-count-badge.long {
	padding: 2px 3px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* ---------- Icon label ---------- */

.monaco-icon-label {
	display: flex; /* required for icons support :before rule */
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-icon-label::before {

	/* svg icons rendered as background image */
	background-size: 16px;
	background-position: left center;
	background-repeat: no-repeat;
	padding-right: 6px;
	width: 16px;
	height: 22px;
	line-height: inherit !important;
	display: inline-block;

	/* fonts icons */
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	vertical-align: top;

	flex-shrink: 0; /* fix for https://github.com/microsoft/vscode/issues/13787 */
}

.monaco-icon-label > .monaco-icon-label-container {
	min-width: 0;
	overflow: hidden;
	text-overflow: ellipsis;
	flex: 1;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name {
	color: inherit;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name > .label-separator {
	margin: 0 2px;
	opacity: 0.5;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .7;
	margin-left: 0.5em;
	font-size: 0.9em;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label.nowrap > .monaco-icon-label-container > .monaco-icon-description-container > .label-description{
	white-space: nowrap
}

.vs .monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .95;
}

.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	font-style: italic;
}

.monaco-icon-label.deprecated {
	text-decoration: line-through;
	opacity: 0.66;
}

/* make sure apply italic font style to decorations as well */
.monaco-icon-label.italic::after {
	font-style: italic;
}

.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	text-decoration: line-through;
}

.monaco-icon-label::after {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	margin: auto 16px 0 5px; /* https://github.com/microsoft/vscode/issues/113223 */
	text-align: center;
}

/* make sure selection color wins when a label is being selected */
.monaco-list:focus .selected .monaco-icon-label, /* list */
.monaco-list:focus .selected .monaco-icon-label::after
{
	color: inherit !important;
}

.monaco-list-row.focused.selected .label-description,
.monaco-list-row.selected .label-description {
	opacity: .8;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-hover {
	cursor: default;
	position: absolute;
	overflow: hidden;
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	box-sizing: initial;
	animation: fadein 100ms linear;
	line-height: 1.5em;
}

.monaco-hover.hidden {
	display: none;
}

.monaco-hover .hover-contents:not(.html-hover-contents) {
	padding: 4px 8px;
}

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) {
	max-width: 500px;
	word-wrap: break-word;
}

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) hr {
	min-width: 100%;
}

.monaco-hover p,
.monaco-hover .code,
.monaco-hover ul {
	margin: 8px 0;
}

.monaco-hover code {
	font-family: var(--monaco-monospace-font);
}

.monaco-hover hr {
	box-sizing: border-box;
	border-left: 0px;
	border-right: 0px;
	margin-top: 4px;
	margin-bottom: -4px;
	margin-left: -8px;
	margin-right: -8px;
	height: 1px;
}

.monaco-hover p:first-child,
.monaco-hover .code:first-child,
.monaco-hover ul:first-child {
	margin-top: 0;
}

.monaco-hover p:last-child,
.monaco-hover .code:last-child,
.monaco-hover ul:last-child {
	margin-bottom: 0;
}

/* MarkupContent Layout */
.monaco-hover ul {
	padding-left: 20px;
}
.monaco-hover ol {
	padding-left: 20px;
}

.monaco-hover li > p {
	margin-bottom: 0;
}

.monaco-hover li > ul {
	margin-top: 0;
}

.monaco-hover code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-hover .monaco-tokenized-source {
	white-space: pre-wrap;
}

.monaco-hover .hover-row.status-bar {
	font-size: 12px;
	line-height: 22px;
}

.monaco-hover .hover-row.status-bar .actions {
	display: flex;
	padding: 0px 8px;
}

.monaco-hover .hover-row.status-bar .actions .action-container {
	margin-right: 16px;
	cursor: pointer;
}

.monaco-hover .hover-row.status-bar .actions .action-container .action .icon {
	padding-right: 4px;
}

.monaco-hover .markdown-hover .hover-contents .codicon {
	color: inherit;
	font-size: inherit;
	vertical-align: middle;
}

.monaco-hover .hover-contents a.code-link:hover,
.monaco-hover .hover-contents a.code-link {
	color: inherit;
}

.monaco-hover .hover-contents a.code-link:before {
	content: '(';
}

.monaco-hover .hover-contents a.code-link:after {
	content: ')';
}

.monaco-hover .hover-contents a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}

/** Spans in markdown hovers need a margin-bottom to avoid looking cramped: https://github.com/microsoft/vscode/issues/101496 **/
.monaco-hover .markdown-hover .hover-contents:not(.code-hover-contents):not(.html-hover-contents) span {
	margin-bottom: 4px;
	display: inline-block;
}

.monaco-hover-content .action-container a {
	-webkit-user-select: none;
	user-select: none;
}

.monaco-hover-content .action-container.disabled {
	pointer-events: none;
	opacity: 0.4;
	cursor: default;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.colorpicker-widget {
	height: 190px;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .colorpicker-hover:focus {
	outline: none;
}


/* Header */

.colorpicker-header {
	display: flex;
	height: 24px;
	position: relative;
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=");
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-header .picked-color {
	width: 216px;
	display: flex;
	align-items: center;
	justify-content: center;
	line-height: 24px;
	cursor: pointer;
	color: white;
	flex: 1;
}

.colorpicker-header .picked-color .codicon {
	color: inherit;
	font-size: 14px;
	position: absolute;
	left: 8px;
}

.colorpicker-header .picked-color.light {
	color: black;
}

.colorpicker-header .original-color {
	width: 74px;
	z-index: inherit;
	cursor: pointer;
}


/* Body */

.colorpicker-body {
	display: flex;
	padding: 8px;
	position: relative;
}

.colorpicker-body .saturation-wrap {
	overflow: hidden;
	height: 150px;
	position: relative;
	min-width: 220px;
	flex: 1;
}

.colorpicker-body .saturation-box {
	height: 150px;
	position: absolute;
}

.colorpicker-body .saturation-selection {
	width: 9px;
	height: 9px;
	margin: -5px 0 0 -5px;
	border: 1px solid rgb(255, 255, 255);
	border-radius: 100%;
	box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.8);
	position: absolute;
}

.colorpicker-body .strip {
	width: 25px;
	height: 150px;
}

.colorpicker-body .hue-strip {
	position: relative;
	margin-left: 8px;
	cursor: grab;
	background: linear-gradient(to bottom, #ff0000 0%, #ffff00 17%, #00ff00 33%, #00ffff 50%, #0000ff 67%, #ff00ff 83%, #ff0000 100%);
}

.colorpicker-body .opacity-strip {
	position: relative;
	margin-left: 8px;
	cursor: grab;
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=");
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-body .strip.grabbing {
	cursor: grabbing;
}

.colorpicker-body .slider {
	position: absolute;
	top: 0;
	left: -2px;
	width: calc(100% + 4px);
	height: 4px;
	box-sizing: border-box;
	border: 1px solid rgba(255, 255, 255, 0.71);
	box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.85);
}

.colorpicker-body .strip .overlay {
	height: 150px;
	pointer-events: none;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* marker zone */

.monaco-editor .peekview-widget .head .peekview-title .severity-icon {
	display: inline-block;
	vertical-align: text-top;
	margin-right: 4px;
}

.monaco-editor .marker-widget {
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .marker-widget > .stale {
	opacity: 0.6;
	font-style: italic;
}

.monaco-editor .marker-widget .title {
	display: inline-block;
	padding-right: 5px;
}

.monaco-editor .marker-widget .descriptioncontainer {
	position: absolute;
	white-space: pre;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 8px 12px 0 20px;
}

.monaco-editor .marker-widget .descriptioncontainer .message {
	display: flex;
	flex-direction: column;
}

.monaco-editor .marker-widget .descriptioncontainer .message .details {
	padding-left: 6px;
}

.monaco-editor .marker-widget .descriptioncontainer .message .source,
.monaco-editor .marker-widget .descriptioncontainer .message span.code {
	opacity: 0.6;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link {
	opacity: 0.6;
	color: inherit;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:before {
	content: '(';
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:after {
	content: ')';
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}

.monaco-editor .marker-widget .descriptioncontainer .filename {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .snippet-placeholder {
	min-width: 2px;
	outline-style: solid;
	outline-width: 1px;
}

.monaco-editor .finish-snippet-placeholder {
	outline-style: solid;
	outline-width: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@font-face {
	font-family: "codicon";
	font-display: block;
	src: url(/assets/webpack/codicon.ff6b888d.ttf) format("truetype");
}

.codicon[class*='codicon-'] {
	font: normal normal normal 16px/1 codicon;
	display: inline-block;
	text-decoration: none;
	text-rendering: auto;
	text-align: center;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/* icon rules are dynamically created in codiconStyles */
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.codicon-wrench-subaction {
	opacity: 0.5;
}

@keyframes codicon-spin {
	100% {
		transform:rotate(360deg);
	}
}

.codicon-sync.codicon-modifier-spin,
.codicon-loading.codicon-modifier-spin,
.codicon-gear.codicon-modifier-spin,
.codicon-notebook-state-executing.codicon-modifier-spin {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.5s steps(30) infinite;
}

.codicon-modifier-disabled {
	opacity: 0.4;
}

/* custom speed & easing for loading icon */
.codicon-loading,
.codicon-tree-item-loading::before {
	animation-duration: 1s !important;
	animation-timing-function: cubic-bezier(0.53, 0.21, 0.29, 0.67) !important;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Suggest widget*/

.monaco-editor .suggest-widget {
	width: 430px;
	z-index: 40;
	display: flex;
	flex-direction: column;
}

.monaco-editor .suggest-widget.message {
	flex-direction: row;
	align-items: center;
}

.monaco-editor .suggest-widget,
.monaco-editor .suggest-details {
	flex: 0 1 auto;
	width: 100%;
	border-style: solid;
	border-width: 1px;
}

.monaco-editor.hc-black .suggest-widget,
.monaco-editor.hc-black .suggest-details {
	border-width: 2px;
}

/* Styles for status bar part */


.monaco-editor .suggest-widget .suggest-status-bar {
	box-sizing: border-box;
	display: none;
	flex-flow: row nowrap;
	justify-content: space-between;
	width: 100%;
	font-size: 80%;
	padding: 0 4px 0 4px;
	border-top: 1px solid transparent;
	overflow: hidden;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar {
	display: flex;
}

.monaco-editor .suggest-widget .suggest-status-bar .left {
	padding-right: 8px;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-label {
	opacity: 0.5;
	color: inherit;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-item:not(:last-of-type) .action-label {
	margin-right: 0;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-item:not(:last-of-type) .action-label::after {
	content: ', ';
	margin-right: 0.3em;
}

.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row>.contents>.main>.right>.readMore,
.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row.focused.string-label>.contents>.main>.right>.readMore {
	display: none;
}

.monaco-editor .suggest-widget.with-status-bar:not(.docs-side) .monaco-list .monaco-list-row:hover>.contents>.main>.right.can-expand-details>.details-label {
	width: 100%;
}

/* Styles for Message element for when widget is loading or is empty */

.monaco-editor .suggest-widget>.message {
	padding-left: 22px;
}

/** Styles for the list element **/

.monaco-editor .suggest-widget>.tree {
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-widget .monaco-list {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/** Styles for each row in the list element **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row {
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	padding-right: 10px;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
	cursor: pointer;
	touch-action: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents {
	flex: 1;
	height: 100%;
	overflow: hidden;
	padding-left: 2px;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main {
	display: flex;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: pre;
	justify-content: space-between;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left, .monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right {
	display: flex;
}

.monaco-editor .suggest-widget:not(.frozen) .monaco-highlighted-label .highlight {
	font-weight: bold;
}

/** ReadMore Icon styles **/

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore::before {
	color: inherit;
	opacity: 1;
	font-size: 14px;
	cursor: pointer;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close {
	position: absolute;
	top: 6px;
	right: 2px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close:hover,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore:hover {
	opacity: 1;
}

/** signature, qualifier, type/details opacity **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	opacity: 0.7;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.signature-label {
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.6;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.qualifier-label {
	margin-left: 12px;
	opacity: 0.4;
	font-size: 85%;
	line-height: initial;
	text-overflow: ellipsis;
	overflow: hidden;
	align-self: center;
}

/** Type Info and icon next to the label in the focused completion item **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	font-size: 85%;
	margin-left: 1.1em;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label>.monaco-tokenized-source {
	display: inline;
}

/** Details: if using CompletionItem#details, show on focus **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	display: none;
}

.monaco-editor .suggest-widget:not(.shows-details) .monaco-list .monaco-list-row.focused>.contents>.main>.right>.details-label {
	display: inline;
}

/** Details: if using CompletionItemLabel#details, always show **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label)>.contents>.main>.right>.details-label,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused:not(.string-label)>.contents>.main>.right>.details-label {
	display: inline;
}

/** Ellipsis on hover **/

.monaco-editor .suggest-widget:not(.docs-side) .monaco-list .monaco-list-row:hover>.contents>.main>.right.can-expand-details>.details-label {
	width: calc(100% - 26px);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left {
	flex-shrink: 1;
	flex-grow: 1;
	overflow: hidden;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.monaco-icon-label {
	flex-shrink: 0;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label)>.contents>.main>.left>.monaco-icon-label {
	max-width: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label>.contents>.main>.left>.monaco-icon-label {
	flex-shrink: 1;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right {
	overflow: hidden;
	flex-shrink: 4;
	max-width: 70%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: inline-block;
	position: absolute;
	right: 10px;
	width: 18px;
	height: 18px;
	visibility: hidden;
}

/** Do NOT display ReadMore when docs is side/below **/

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row>.contents>.main>.right>.readMore, .monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: none !important;
}

/** Do NOT display ReadMore when using plain CompletionItemLabel (details/documentation might not be resolved) **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label>.contents>.main>.right>.readMore {
	display: none;
}

/** Focused item can show ReadMore, but can't when docs is side/below **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused.string-label>.contents>.main>.right>.readMore {
	display: inline-block;
}

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row>.contents>.main>.right>.readMore,
.monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:hover>.contents>.main>.right>.readMore {
	visibility: visible;
}

/** Styles for each row in the list **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated {
	opacity: 0.66;
	text-decoration: unset;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated>.monaco-icon-label-container>.monaco-icon-name-container {
	text-decoration: line-through;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label::before {
	height: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon {
	display: block;
	height: 16px;
	width: 16px;
	margin-left: 2px;
	background-repeat: no-repeat;
	background-size: 80%;
	background-position: center;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.hide {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .suggest-icon {
	display: flex;
	align-items: center;
	margin-right: 4px;
}

.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .icon, .monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .suggest-icon::before {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customcolor .colorspan {
	margin: 0 0 0 0.3em;
	border: 0.1em solid #000;
	width: 0.7em;
	height: 0.7em;
	display: inline-block;
}

/** Styles for the docs of the completion item in focus **/

.monaco-editor .suggest-details-container {
	z-index: 41;
}

.monaco-editor .suggest-details {
	display: flex;
	flex-direction: column;
	cursor: default;
}

.monaco-editor .suggest-details.no-docs {
	display: none;
}

.monaco-editor .suggest-details>.monaco-scrollable-element {
	flex: 1;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body {
	box-sizing: border-box;
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.type {
	flex: 2;
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.7;
	white-space: pre;
	margin: 0 24px 0 0;
	padding: 4px 0 12px 5px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.type.auto-wrap {
	white-space: normal;
	word-break: break-all;
}


.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs {
	margin: 0;
	padding: 4px 5px;
	white-space: pre-wrap;
}

.monaco-editor .suggest-details.no-type>.monaco-scrollable-element>.body>.docs {
	margin-right: 24px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs {
	padding: 0;
	white-space: initial;
	min-height: calc(1rem + 8px);
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div,
.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>span:not(:empty) {
	padding: 4px 5px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div>p:first-child {
	margin-top: 0;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div>p:last-child {
	margin-bottom: 0;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs .monaco-tokenized-source {
	white-space: pre;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs .code {
	white-space: pre-wrap;
	word-wrap: break-word;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs .codicon {
	vertical-align: sub;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>p:empty {
	display: none;
}

.monaco-editor .suggest-details code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .suggest-details ul {
	padding-left: 20px;
}

.monaco-editor .suggest-details ol {
	padding-left: 20px;
}

.monaco-editor .suggest-details p code {
	font-family: var(--monaco-monospace-font);
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .suggest-preview-additional-widget {
	white-space: nowrap;
}

.monaco-editor .suggest-preview-additional-widget .content-spacer {
	color: transparent;
	white-space: pre;
}

.monaco-editor .suggest-preview-additional-widget .button {
	display: inline-block;
	cursor: pointer;
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .ghost-text-hidden {
	opacity: 0;
	font-size: 0;
}

.monaco-editor .ghost-text-decoration {
	font-style: italic;
}

.monaco-editor .suggest-preview-text {
	font-style: italic;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor.vs .dnd-target {
	border-right: 2px dotted black;
	color: white; /* opposite of black */
}
.monaco-editor.vs-dark .dnd-target {
	border-right: 2px dotted #AEAFAD;
	color: #51504f; /* opposite of #AEAFAD */
}
.monaco-editor.hc-black .dnd-target {
	border-right: 2px dotted #fff;
	color: #000; /* opposite of #fff */
}

.monaco-editor.mouse-default .view-lines,
.monaco-editor.vs-dark.mac.mouse-default .view-lines,
.monaco-editor.hc-black.mac.mouse-default .view-lines {
	cursor: default;
}
.monaco-editor.mouse-copy .view-lines,
.monaco-editor.vs-dark.mac.mouse-copy .view-lines,
.monaco-editor.hc-black.mac.mouse-copy .view-lines {
	cursor: copy;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-custom-checkbox {
	margin-left: 2px;
	float: left;
	cursor: pointer;
	overflow: hidden;
	opacity: 0.7;
	width: 20px;
	height: 20px;
	border: 1px solid transparent;
	padding: 1px;
	box-sizing:	border-box;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-custom-checkbox:hover,
.monaco-custom-checkbox.checked {
	opacity: 1;
}

.hc-black .monaco-custom-checkbox {
	background: none;
}

.hc-black .monaco-custom-checkbox:hover {
	background: none;
}

.monaco-custom-checkbox.monaco-simple-checkbox {
	height: 18px;
	width: 18px;
	border: 1px solid transparent;
	border-radius: 3px;
	margin-right: 9px;
	margin-left: 0px;
	padding: 0px;
	opacity: 1;
	background-size: 16px !important;
}

/* hide check when unchecked */
.monaco-custom-checkbox.monaco-simple-checkbox:not(.checked)::before {
	visibility: hidden;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Find widget */
.monaco-editor .find-widget {
	position: absolute;
	z-index: 35;
	height: 33px;
	overflow: hidden;
	line-height: 19px;
	transition: transform 200ms linear;
	padding: 0 4px;
	box-sizing: border-box;
	transform: translateY(calc(-100% - 10px)); /* shadow (10px) */
}

.monaco-editor .find-widget textarea {
	margin: 0px;
}

.monaco-editor .find-widget.hiddenEditor {
	display: none;
}

/* Find widget when replace is toggled on */
.monaco-editor .find-widget.replaceToggled > .replace-part {
	display: flex;
}

.monaco-editor .find-widget.visible  {
	transform: translateY(0);
}

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus {
	outline: 1px solid -webkit-focus-ring-color;
	outline-offset: -1px;
}

.monaco-editor .find-widget .monaco-inputbox .input {
	background-color: transparent;
	min-height: 0;
}

.monaco-editor .find-widget .monaco-findInput .input {
	font-size: 13px;
}

.monaco-editor .find-widget > .find-part,
.monaco-editor .find-widget > .replace-part {
	margin: 4px 0 0 17px;
	font-size: 12px;
	display: flex;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox,
.monaco-editor .find-widget > .replace-part .monaco-inputbox {
	min-height: 25px;
}


.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .mirror {
	padding-right: 22px;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .input,
.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .mirror,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .input,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .mirror {
	padding-top: 2px;
	padding-bottom: 2px;
}

.monaco-editor .find-widget > .find-part .find-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget > .replace-part .replace-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget .monaco-findInput {
	vertical-align: middle;
	display: flex;
	flex:1;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element {
	/* Make sure textarea inherits the width correctly */
	width: 100%;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element .scrollbar.vertical {
	/* Hide vertical scrollbar */
	opacity: 0;
}

.monaco-editor .find-widget .matchesCount {
	display: flex;
	flex: initial;
	margin: 0 0 0 3px;
	padding: 2px 0 0 2px;
	height: 25px;
	vertical-align: middle;
	box-sizing: border-box;
	text-align: center;
	line-height: 23px;
}

.monaco-editor .find-widget .button {
	width: 16px;
	height: 16px;
	padding: 3px;
	border-radius: 5px;
	display: flex;
	flex: initial;
	margin-left: 3px;
	background-position: center center;
	background-repeat: no-repeat;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
}

/* find in selection button */
.monaco-editor .find-widget .codicon-find-selection {
	width: 22px;
	height: 22px;
	padding: 3px;
	border-radius: 5px;
}

.monaco-editor .find-widget .button.left {
	margin-left: 0;
	margin-right: 3px;
}

.monaco-editor .find-widget .button.wide {
	width: auto;
	padding: 1px 6px;
	top: -1px;
}

.monaco-editor .find-widget .button.toggle {
	position: absolute;
	top: 0;
	left: 3px;
	width: 18px;
	height: 100%;
	border-radius: 0;
	box-sizing: border-box;
}

.monaco-editor .find-widget .button.toggle.disabled {
	display: none;
}

.monaco-editor .find-widget .disabled {
	opacity: 0.3;
	cursor: default;
}

.monaco-editor .find-widget > .replace-part {
	display: none;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput {
	position: relative;
	display: flex;
	vertical-align: middle;
	flex: auto;
	flex-grow: 0;
	flex-shrink: 0;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

/* REDUCED */
.monaco-editor .find-widget.reduced-find-widget .matchesCount {
	display:none;
}

/* NARROW (SMALLER THAN REDUCED) */
.monaco-editor .find-widget.narrow-find-widget {
	max-width: 257px !important;
}

/* COLLAPSED (SMALLER THAN NARROW) */
.monaco-editor .find-widget.collapsed-find-widget {
	max-width: 170px !important;
}

.monaco-editor .find-widget.collapsed-find-widget .button.previous,
.monaco-editor .find-widget.collapsed-find-widget .button.next,
.monaco-editor .find-widget.collapsed-find-widget .button.replace,
.monaco-editor .find-widget.collapsed-find-widget .button.replace-all,
.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-findInput .controls {
	display:none;
}

.monaco-editor .findMatch {
	animation-duration: 0;
	animation-name: inherit !important;
}

.monaco-editor .find-widget .monaco-sash {
	left: 0 !important;
}

.monaco-editor.hc-black .find-widget .button:before {
	position: relative;
	top: 1px;
	left: 2px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-inputbox {
	position: relative;
	display: block;
	padding: 0;
	box-sizing:	border-box;

	/* Customizable */
	font-size: inherit;
}

.monaco-inputbox.idle {
	border: 1px solid transparent;
}

.monaco-inputbox > .ibwrapper > .input,
.monaco-inputbox > .ibwrapper > .mirror {

	/* Customizable */
	padding: 4px;
}

.monaco-inputbox > .ibwrapper {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-inputbox > .ibwrapper > .input {
	display: inline-block;
	box-sizing:	border-box;
	width: 100%;
	height: 100%;
	line-height: inherit;
	border: none;
	font-family: inherit;
	font-size: inherit;
	resize: none;
	color: inherit;
}

.monaco-inputbox > .ibwrapper > input {
	text-overflow: ellipsis;
}

.monaco-inputbox > .ibwrapper > textarea.input {
	display: block;
	-ms-overflow-style: none; /* IE 10+: hide scrollbars */
	scrollbar-width: none; /* Firefox: hide scrollbars */
	outline: none;
}

.monaco-inputbox > .ibwrapper > textarea.input::-webkit-scrollbar {
	display: none; /* Chrome + Safari: hide scrollbar */
}

.monaco-inputbox > .ibwrapper > textarea.input.empty {
	white-space: nowrap;
}

.monaco-inputbox > .ibwrapper > .mirror {
	position: absolute;
	display: inline-block;
	width: 100%;
	top: 0;
	left: 0;
	box-sizing: border-box;
	white-space: pre-wrap;
	visibility: hidden;
	word-wrap: break-word;
}

/* Context view */

.monaco-inputbox-container {
	text-align: right;
}

.monaco-inputbox-container .monaco-inputbox-message {
	display: inline-block;
	overflow: hidden;
	text-align: left;
	width: 100%;
	box-sizing:	border-box;
	padding: 0.4em;
	font-size: 12px;
	line-height: 17px;
	margin-top: -1px;
	word-wrap: break-word;
}

/* Action bar support */
.monaco-inputbox .monaco-action-bar {
	position: absolute;
	right: 2px;
	top: 4px;
}

.monaco-inputbox .monaco-action-bar .action-item {
	margin-left: 2px;
}

.monaco-inputbox .monaco-action-bar .action-item .codicon {
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- Find input ---------- */

.monaco-findInput {
	position: relative;
}

.monaco-findInput .monaco-inputbox {
	font-size: 13px;
	width: 100%;
}

.monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

.vs .monaco-findInput.disabled {
	background-color: #E1E1E1;
}

/* Theming */
.vs-dark .monaco-findInput.disabled {
	background-color: #333;
}

/* Highlighting */
.monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-0 100ms linear 0s;
}
.monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-1 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-0 .controls,
.vs-dark  .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-dark-0 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-1 .controls,
.vs-dark  .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-dark-1 100ms linear 0s;
}

@keyframes monaco-findInput-highlight-0 {
	0% { background: rgba(253, 255, 0, 0.8); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-1 {
	0% { background: rgba(253, 255, 0, 0.8); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {
	0% { background: rgba(255, 255, 255, 0.44); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-dark-1 {
	0% { background: rgba(255, 255, 255, 0.44); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .codicon-folding-expanded,
.monaco-editor .margin-view-overlays .codicon-folding-collapsed {
	cursor: pointer;
	opacity: 0;
	transition: opacity 0.5s;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 140%;
	margin-left: 2px;
}

.monaco-editor .margin-view-overlays:hover .codicon,
.monaco-editor .margin-view-overlays .codicon.codicon-folding-collapsed,
.monaco-editor .margin-view-overlays .codicon.alwaysShowFoldIcons {
	opacity: 1;
}

.monaco-editor .inline-folded:after {
	color: grey;
	margin: 0.1em 0.2em 0 0.2em;
	content: "⋯";
	display: inline;
	line-height: 1em;
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .iPadShowKeyboard {
	width: 58px;
	min-width: 0;
	height: 36px;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	resize: none;
	overflow: hidden;
	background: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCA1MyAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwKSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNDguMDM2NCA0LjAxMDQySDQuMDA3NzlMNC4wMDc3OSAzMi4wMjg2SDQ4LjAzNjRWNC4wMTA0MlpNNC4wMDc3OSAwLjAwNzgxMjVDMS43OTcyMSAwLjAwNzgxMjUgMC4wMDUxODc5OSAxLjc5OTg0IDAuMDA1MTg3OTkgNC4wMTA0MlYzMi4wMjg2QzAuMDA1MTg3OTkgMzQuMjM5MiAxLjc5NzIxIDM2LjAzMTIgNC4wMDc3OSAzNi4wMzEySDQ4LjAzNjRDNTAuMjQ3IDM2LjAzMTIgNTIuMDM5IDM0LjIzOTIgNTIuMDM5IDMyLjAyODZWNC4wMTA0MkM1Mi4wMzkgMS43OTk4NCA1MC4yNDcgMC4wMDc4MTI1IDQ4LjAzNjQgMC4wMDc4MTI1SDQuMDA3NzlaTTguMDEwNDIgOC4wMTMwMkgxMi4wMTNWMTIuMDE1Nkg4LjAxMDQyVjguMDEzMDJaTTIwLjAxODIgOC4wMTMwMkgxNi4wMTU2VjEyLjAxNTZIMjAuMDE4MlY4LjAxMzAyWk0yNC4wMjA4IDguMDEzMDJIMjguMDIzNFYxMi4wMTU2SDI0LjAyMDhWOC4wMTMwMlpNMzYuMDI4NiA4LjAxMzAySDMyLjAyNlYxMi4wMTU2SDM2LjAyODZWOC4wMTMwMlpNNDAuMDMxMiA4LjAxMzAySDQ0LjAzMzlWMTIuMDE1Nkg0MC4wMzEyVjguMDEzMDJaTTE2LjAxNTYgMTYuMDE4Mkg4LjAxMDQyVjIwLjAyMDhIMTYuMDE1NlYxNi4wMTgyWk0yMC4wMTgyIDE2LjAxODJIMjQuMDIwOFYyMC4wMjA4SDIwLjAxODJWMTYuMDE4MlpNMzIuMDI2IDE2LjAxODJIMjguMDIzNFYyMC4wMjA4SDMyLjAyNlYxNi4wMTgyWk00NC4wMzM5IDE2LjAxODJWMjAuMDIwOEgzNi4wMjg2VjE2LjAxODJINDQuMDMzOVpNMTIuMDEzIDI0LjAyMzRIOC4wMTA0MlYyOC4wMjZIMTIuMDEzVjI0LjAyMzRaTTE2LjAxNTYgMjQuMDIzNEgzNi4wMjg2VjI4LjAyNkgxNi4wMTU2VjI0LjAyMzRaTTQ0LjAzMzkgMjQuMDIzNEg0MC4wMzEyVjI4LjAyNkg0NC4wMzM5VjI0LjAyMzRaIiBmaWxsPSIjNDI0MjQyIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDAiPgo8cmVjdCB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==") center center no-repeat;
	border: 4px solid #F6F6F6;
	border-radius: 4px;
}

.monaco-editor.vs-dark .iPadShowKeyboard {
	background: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCA1MyAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwKSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNDguMDM2NCA0LjAxMDQySDQuMDA3NzlMNC4wMDc3OSAzMi4wMjg2SDQ4LjAzNjRWNC4wMTA0MlpNNC4wMDc3OSAwLjAwNzgxMjVDMS43OTcyMSAwLjAwNzgxMjUgMC4wMDUxODc5OSAxLjc5OTg0IDAuMDA1MTg3OTkgNC4wMTA0MlYzMi4wMjg2QzAuMDA1MTg3OTkgMzQuMjM5MiAxLjc5NzIxIDM2LjAzMTIgNC4wMDc3OSAzNi4wMzEySDQ4LjAzNjRDNTAuMjQ3IDM2LjAzMTIgNTIuMDM5IDM0LjIzOTIgNTIuMDM5IDMyLjAyODZWNC4wMTA0MkM1Mi4wMzkgMS43OTk4NCA1MC4yNDcgMC4wMDc4MTI1IDQ4LjAzNjQgMC4wMDc4MTI1SDQuMDA3NzlaTTguMDEwNDIgOC4wMTMwMkgxMi4wMTNWMTIuMDE1Nkg4LjAxMDQyVjguMDEzMDJaTTIwLjAxODIgOC4wMTMwMkgxNi4wMTU2VjEyLjAxNTZIMjAuMDE4MlY4LjAxMzAyWk0yNC4wMjA4IDguMDEzMDJIMjguMDIzNFYxMi4wMTU2SDI0LjAyMDhWOC4wMTMwMlpNMzYuMDI4NiA4LjAxMzAySDMyLjAyNlYxMi4wMTU2SDM2LjAyODZWOC4wMTMwMlpNNDAuMDMxMiA4LjAxMzAySDQ0LjAzMzlWMTIuMDE1Nkg0MC4wMzEyVjguMDEzMDJaTTE2LjAxNTYgMTYuMDE4Mkg4LjAxMDQyVjIwLjAyMDhIMTYuMDE1NlYxNi4wMTgyWk0yMC4wMTgyIDE2LjAxODJIMjQuMDIwOFYyMC4wMjA4SDIwLjAxODJWMTYuMDE4MlpNMzIuMDI2IDE2LjAxODJIMjguMDIzNFYyMC4wMjA4SDMyLjAyNlYxNi4wMTgyWk00NC4wMzM5IDE2LjAxODJWMjAuMDIwOEgzNi4wMjg2VjE2LjAxODJINDQuMDMzOVpNMTIuMDEzIDI0LjAyMzRIOC4wMTA0MlYyOC4wMjZIMTIuMDEzVjI0LjAyMzRaTTE2LjAxNTYgMjQuMDIzNEgzNi4wMjg2VjI4LjAyNkgxNi4wMTU2VjI0LjAyMzRaTTQ0LjAzMzkgMjQuMDIzNEg0MC4wMzEyVjI4LjAyNkg0NC4wMzM5VjI0LjAyMzRaIiBmaWxsPSIjQzVDNUM1Ii8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDAiPgo8cmVjdCB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==") center center no-repeat;
	border: 4px solid #252526;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .tokens-inspect-widget {
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 10px;
}

.tokens-inspect-separator {
	height: 1px;
	border: 0;
}

.monaco-editor .tokens-inspect-widget .tm-token {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .tokens-inspect-widget .tm-token-length {
	font-weight: normal;
	font-size: 60%;
	float: right;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-table {
	width: 100%;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-value {
	font-family: var(--monaco-monospace-font);
	text-align: right;
}

.monaco-editor .tokens-inspect-widget .tm-token-type {
	font-family: var(--monaco-monospace-font);
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .detected-link,
.monaco-editor .detected-link-active {
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .detected-link-active {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .parameter-hints-widget {
	z-index: 10;
	display: flex;
	flex-direction: column;
	line-height: 1.5em;
}

.monaco-editor .parameter-hints-widget > .phwrapper {
	max-width: 440px;
	display: flex;
	flex-direction: row;
}

.monaco-editor .parameter-hints-widget.multiple {
	min-height: 3.3em;
	padding: 0;
}

.monaco-editor .parameter-hints-widget.visible {
	transition: left .05s ease-in-out;
}

.monaco-editor .parameter-hints-widget p,
.monaco-editor .parameter-hints-widget ul {
	margin: 8px 0;
}

.monaco-editor .parameter-hints-widget .monaco-scrollable-element,
.monaco-editor .parameter-hints-widget .body {
	display: flex;
	flex: 1;
	flex-direction: column;
	min-height: 100%;
}

.monaco-editor .parameter-hints-widget .signature {
	padding: 4px 5px;
}

.monaco-editor .parameter-hints-widget .docs {
	padding: 0 10px 0 5px;
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs.empty {
	display: none;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs {
	white-space: initial;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs code {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .docs .code {
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .parameter-hints-widget .controls {
	display: none;
	flex-direction: column;
	align-items: center;
	min-width: 22px;
	justify-content: flex-end;
}

.monaco-editor .parameter-hints-widget.multiple .controls {
	display: flex;
	padding: 0 2px;
}

.monaco-editor .parameter-hints-widget.multiple .button {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	cursor: pointer;
}

.monaco-editor .parameter-hints-widget .button.previous {
	bottom: 24px;
}

.monaco-editor .parameter-hints-widget .overloads {
	text-align: center;
	height: 12px;
	line-height: 12px;
	opacity: 0.5;
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .signature .parameter.active {
	font-weight: bold;
}

.monaco-editor .parameter-hints-widget .documentation-parameter > .parameter {
	font-weight: bold;
	margin-right: 0.5em;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .rename-box {
	z-index: 100;
	color: inherit;
}

.monaco-editor .rename-box.preview {
	padding: 3px 3px 0 3px;
}

.monaco-editor .rename-box .rename-input {
	padding: 3px;
	width: calc(100% - 6px);
}

.monaco-editor .rename-box .rename-label {
	display: none;
	opacity: .8;
}

.monaco-editor .rename-box.preview .rename-label {
	display: inherit;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


/* Default standalone editor fonts */
.monaco-editor {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC", "Segoe UI", "HelveticaNeue-Light", system-ui, "Ubuntu", "Droid Sans", sans-serif;
	--monaco-monospace-font: "SF Mono", Monaco, Menlo, Consolas, "Ubuntu Mono", "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace;
}

.monaco-menu .monaco-action-bar.vertical .action-item .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-hover p {
	margin: 0;
}

/* See https://github.com/microsoft/monaco-editor/issues/2168#issuecomment-780078600 */
.monaco-aria-container {
	position: absolute !important;
	top: 0; /* avoid being placed underneath a sibling element */
	height: 1px;
	width: 1px;
	margin: -1px;
	overflow: hidden;
	padding: 0;
	clip: rect(1px, 1px, 1px, 1px);
	clip-path: inset(50%);
}

/* The hc-black theme is already high contrast optimized */
.monaco-editor.hc-black {
	-ms-high-contrast-adjust: none;
}
/* In case the browser goes into high contrast mode and the editor is not configured with the hc-black theme */
@media screen and (-ms-high-contrast:active) {

	/* current line highlight */
	.monaco-editor.vs .view-overlays .current-line,
	.monaco-editor.vs-dark .view-overlays .current-line {
		border-color: windowtext !important;
		border-left: 0;
		border-right: 0;
	}

	/* view cursors */
	.monaco-editor.vs .cursor,
	.monaco-editor.vs-dark .cursor {
		background-color: windowtext !important;
	}
	/* dnd target */
	.monaco-editor.vs .dnd-target,
	.monaco-editor.vs-dark .dnd-target {
		border-color: windowtext !important;
	}

	/* selected text background */
	.monaco-editor.vs .selected-text,
	.monaco-editor.vs-dark .selected-text {
		background-color: highlight !important;
	}

	/* allow the text to have a transparent background. */
	.monaco-editor.vs .view-line,
	.monaco-editor.vs-dark .view-line {
		-ms-high-contrast-adjust: none;
	}

	/* text color */
	.monaco-editor.vs .view-line span,
	.monaco-editor.vs-dark .view-line span {
		color: windowtext !important;
	}
	/* selected text color */
	.monaco-editor.vs .view-line span.inline-selected-text,
	.monaco-editor.vs-dark .view-line span.inline-selected-text {
		color: highlighttext !important;
	}

	/* allow decorations */
	.monaco-editor.vs .view-overlays,
	.monaco-editor.vs-dark .view-overlays {
		-ms-high-contrast-adjust: none;
	}

	/* various decorations */
	.monaco-editor.vs .selectionHighlight,
	.monaco-editor.vs-dark .selectionHighlight,
	.monaco-editor.vs .wordHighlight,
	.monaco-editor.vs-dark .wordHighlight,
	.monaco-editor.vs .wordHighlightStrong,
	.monaco-editor.vs-dark .wordHighlightStrong,
	.monaco-editor.vs .reference-decoration,
	.monaco-editor.vs-dark .reference-decoration {
		border: 2px dotted highlight !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .rangeHighlight,
	.monaco-editor.vs-dark .rangeHighlight {
		background: transparent !important;
		border: 1px dotted activeborder !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .bracket-match,
	.monaco-editor.vs-dark .bracket-match {
		border-color: windowtext !important;
		background: transparent !important;
	}

	/* find widget */
	.monaco-editor.vs .findMatch,
	.monaco-editor.vs-dark .findMatch,
	.monaco-editor.vs .currentFindMatch,
	.monaco-editor.vs-dark .currentFindMatch {
		border: 2px dotted activeborder !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .find-widget,
	.monaco-editor.vs-dark .find-widget {
		border: 1px solid windowtext;
	}

	/* list - used by suggest widget */
	.monaco-editor.vs .monaco-list .monaco-list-row,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row.focused,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row:hover,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* scrollbars */
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar {
		-ms-high-contrast-adjust: none;
		background: background !important;
		border: 1px solid windowtext;
		box-sizing: border-box;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
		background: windowtext !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider:hover,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider:hover {
		background: highlight !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider.active,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
		background: highlight !important;
	}

	/* overview ruler */
	.monaco-editor.vs .decorationsOverviewRuler,
	.monaco-editor.vs-dark .decorationsOverviewRuler {
		opacity: 0;
	}

	/* minimap */
	.monaco-editor.vs .minimap,
	.monaco-editor.vs-dark .minimap {
		display: none;
	}

	/* squiggles */
	.monaco-editor.vs .squiggly-d-error,
	.monaco-editor.vs-dark .squiggly-d-error {
		background: transparent !important;
		border-bottom: 4px double #E47777;
	}
	.monaco-editor.vs .squiggly-c-warning,
	.monaco-editor.vs-dark .squiggly-c-warning {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-b-info,
	.monaco-editor.vs-dark .squiggly-b-info {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-a-hint,
	.monaco-editor.vs-dark .squiggly-a-hint {
		border-bottom: 4px double #6c6c6c;
	}

	/* contextmenu */
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
		-ms-high-contrast-adjust: none;
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label {
		-ms-high-contrast-adjust: none;
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* diff editor */
	.monaco-diff-editor.vs .diffOverviewRuler,
	.monaco-diff-editor.vs-dark .diffOverviewRuler {
		display: none;
	}
	.monaco-editor.vs .line-insert,
	.monaco-editor.vs-dark .line-insert,
	.monaco-editor.vs .line-delete,
	.monaco-editor.vs-dark .line-delete {
		background: transparent !important;
		border: 1px solid highlight !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .char-insert,
	.monaco-editor.vs-dark .char-insert,
	.monaco-editor.vs .char-delete,
	.monaco-editor.vs-dark .char-delete {
		background: transparent !important;
	}
}

/*.monaco-editor.vs [tabindex="0"]:focus {
	outline: 1px solid rgba(0, 122, 204, 0.4);
	outline-offset: -1px;
	opacity: 1 !important;
}

.monaco-editor.vs-dark [tabindex="0"]:focus {
	outline: 1px solid rgba(14, 99, 156, 0.6);
	outline-offset: -1px;
	opacity: 1 !important;
}*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- DiffEditor ---------- */

.monaco-diff-editor .diffOverview {
	z-index: 9;
}

.monaco-diff-editor .diffOverview .diffViewport {
	z-index: 10;
}

/* colors not externalized: using transparancy on background */
.monaco-diff-editor.vs			.diffOverview { background: rgba(0, 0, 0, 0.03); }
.monaco-diff-editor.vs-dark		.diffOverview { background: rgba(255, 255, 255, 0.01); }

.monaco-scrollable-element.modified-in-monaco-diff-editor.vs		.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark	.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black	.scrollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider {
	z-index: 10;
}
.modified-in-monaco-diff-editor				.slider.active { background: rgba(171, 171, 171, .4); }
.modified-in-monaco-diff-editor.hc-black	.slider.active { background: none; }

/* ---------- Diff ---------- */

.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign,
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	font-size: 11px !important;
	opacity: 0.7 !important;
	display: flex !important;
	align-items: center;
}
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign {
	opacity: 1;
}

.monaco-editor .inline-deleted-margin-view-zone {
	text-align: right;
}
.monaco-editor .inline-added-margin-view-zone {
	text-align: right;
}

/* ---------- Inline Diff ---------- */

.monaco-editor .view-zones .view-lines .view-line span {
	display: inline-block;
}

.monaco-editor .margin-view-zones .lightbulb-glyph:hover {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-diff-editor .diff-review-line-number {
	text-align: right;
	display: inline-block;
}

.monaco-diff-editor .diff-review {
	position: absolute;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-diff-editor .diff-review-summary {
	padding-left: 10px;
}

.monaco-diff-editor .diff-review-shadow {
	position: absolute;
}

.monaco-diff-editor .diff-review-row {
	white-space: pre;
}

.monaco-diff-editor .diff-review-table {
	display: table;
	min-width: 100%;
}

.monaco-diff-editor .diff-review-row {
	display: table-row;
	width: 100%;
}

.monaco-diff-editor .diff-review-spacer {
	display: inline-block;
	width: 10px;
	vertical-align: middle;
}

.monaco-diff-editor .diff-review-spacer > .codicon {
	font-size: 9px !important;
}

.monaco-diff-editor .diff-review-actions {
	display: inline-block;
	position: absolute;
	right: 10px;
	top: 2px;
}

.monaco-diff-editor .diff-review-actions .action-label {
	width: 16px;
	height: 16px;
	margin: 2px 0;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view {
	position: absolute;
	z-index: 2500;
}

.context-view.fixed {
	all: initial;
	font-family: inherit;
	font-size: 13px;
	position: fixed;
	z-index: 2500;
	color: inherit;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view .monaco-menu {
	min-width: 130px;
}

</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	font-size: 13px;
}

.quick-input-widget .monaco-highlighted-label .highlight,
.quick-input-widget .monaco-highlighted-label .highlight {
	color: #0066BF;
}

.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label .highlight,
.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label .highlight {
	color: #9DDDFF;
}

.vs-dark .quick-input-widget .monaco-highlighted-label .highlight,
.vs-dark .quick-input-widget .monaco-highlighted-label .highlight {
	color: #0097fb;
}

.hc-black .quick-input-widget .monaco-highlighted-label .highlight,
.hc-black .quick-input-widget .monaco-highlighted-label .highlight {
	color: #F38518;
}

.monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(221, 221, 221, 0.4);
	border: solid 1px rgba(204, 204, 204, 0.4);
	border-bottom-color: rgba(187, 187, 187, 0.4);
	box-shadow: inset 0 -1px 0 rgba(187, 187, 187, 0.4);
	color: #555;
}

.hc-black .monaco-keybinding > .monaco-keybinding-key {
	background-color: transparent;
	border: solid 1px rgb(111, 195, 223);
	box-shadow: none;
	color: #fff;
}

.vs-dark .monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(128, 128, 128, 0.17);
	border: solid 1px rgba(51, 51, 51, 0.6);
	border-bottom-color: rgba(68, 68, 68, 0.6);
	box-shadow: inset 0 -1px 0 rgba(68, 68, 68, 0.6);
	color: #ccc;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-text-button {
	box-sizing: border-box;
	display: flex;
	width: 100%;
	padding: 4px;
	text-align: center;
	cursor: pointer;
	justify-content: center;
	align-items: center;
}

.monaco-text-button:focus {
	outline-offset: 2px !important;
}

.monaco-text-button:hover {
	text-decoration: none !important;
}

.monaco-button.disabled:focus,
.monaco-button.disabled {
	opacity: 0.4 !important;
	cursor: default;
}

.monaco-text-button > .codicon {
	margin: 0 0.2em;
	color: inherit !important;
}

.monaco-button-dropdown {
	display: flex;
	cursor: pointer;
}

.monaco-button-dropdown > .monaco-dropdown-button {
	margin-left: 1px;
}

.monaco-description-button {
	flex-direction: column;
}

.monaco-description-button .monaco-button-label {
	font-weight: 500;
}

.monaco-description-button .monaco-button-description {
	font-style: italic;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-progress-container {
	width: 100%;
	height: 5px;
	overflow: hidden; /* keep progress bit in bounds */
}

.monaco-progress-container .progress-bit {
	width: 2%;
	height: 5px;
	position: absolute;
	left: 0;
	display: none;
}

.monaco-progress-container.active .progress-bit {
	display: inherit;
}

.monaco-progress-container.discrete .progress-bit {
	left: 0;
	transition: width 100ms linear;
}

.monaco-progress-container.discrete.done .progress-bit {
	width: 100%;
}

.monaco-progress-container.infinite .progress-bit {
	animation-name: progress;
	animation-duration: 4s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
	transform: translate3d(0px, 0px, 0px);
}

/**
 * The progress bit has a width: 2% (1/50) of the parent container. The animation moves it from 0% to 100% of
 * that container. Since translateX is relative to the progress bit size, we have to multiple it with
 * its relative size to the parent container:
 * parent width: 5000%
 *    bit width: 100%
 * translateX should be as follow:
 *  50%: 5000% * 50% - 50% (set to center) = 2450%
 * 100%: 5000% * 100% - 100% (do not overflow) = 4900%
 */
@keyframes progress { from { transform: translateX(0%) scaleX(1) } 50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4900%) scaleX(1) } }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	position: absolute;
	width: 600px;
	z-index: 2000;
	padding: 0 1px 1px 1px;
	left: 50%;
	margin-left: -300px;
}

.quick-input-titlebar {
	display: flex;
	align-items: center;
}

.quick-input-left-action-bar {
	display: flex;
	margin-left: 4px;
	flex: 1;
}

.quick-input-title {
	padding: 3px 0px;
	text-align: center;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-right-action-bar {
	display: flex;
	margin-right: 4px;
	flex: 1;
}

.quick-input-right-action-bar > .actions-container {
	justify-content: flex-end;
}

.quick-input-titlebar .monaco-action-bar .action-label.codicon {
	background-position: center;
	background-repeat: no-repeat;
	padding: 2px;
}

.quick-input-description {
	margin: 6px;
}

.quick-input-header .quick-input-description {
	margin: 4px 2px;
}

.quick-input-header {
	display: flex;
	padding: 6px 6px 0px 6px;
	margin-bottom: -2px;
}

.quick-input-widget.hidden-input .quick-input-header {
	/* reduce margins and paddings when input box hidden */
	padding: 0;
	margin-bottom: 0;
}

.quick-input-and-message {
	display: flex;
	flex-direction: column;
	flex-grow: 1;
	min-width: 0;
	position: relative;
}

.quick-input-check-all {
	align-self: center;
	margin: 0;
}

.quick-input-filter {
	flex-grow: 1;
	display: flex;
	position: relative;
}

.quick-input-box {
	flex-grow: 1;
}

.quick-input-widget.show-checkboxes .quick-input-box,
.quick-input-widget.show-checkboxes .quick-input-message {
	margin-left: 5px;
}

.quick-input-visible-count {
	position: absolute;
	left: -10000px;
}

.quick-input-count {
	align-self: center;
	position: absolute;
	right: 4px;
	display: flex;
	align-items: center;
}

.quick-input-count .monaco-count-badge {
	vertical-align: middle;
	padding: 2px 4px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}

.quick-input-action {
	margin-left: 6px;
}

.quick-input-action .monaco-text-button {
	font-size: 11px;
	padding: 0 6px;
	display: flex;
	height: 27.5px;
	align-items: center;
}

.quick-input-message {
	margin-top: -1px;
	padding: 5px 5px 2px 5px;
	overflow-wrap: break-word;
}

.quick-input-message > .codicon {
	margin: 0 0.2em;
	vertical-align: text-bottom;
}

.quick-input-progress.monaco-progress-container {
	position: relative;
}

.quick-input-progress.monaco-progress-container,
.quick-input-progress.monaco-progress-container .progress-bit {
	height: 2px;
}

.quick-input-list {
	line-height: 22px;
	margin-top: 6px;
}

.quick-input-widget.hidden-input .quick-input-list {
	margin-top: 0; /* reduce margins when input box hidden */
}

.quick-input-list .monaco-list {
	overflow: hidden;
	max-height: calc(20 * 22px);
}

.quick-input-list .quick-input-list-entry {
	box-sizing: border-box;
	overflow: hidden;
	display: flex;
	height: 100%;
	padding: 0 6px;
}

.quick-input-list .quick-input-list-entry.quick-input-list-separator-border {
	border-top-width: 1px;
	border-top-style: solid;
}

.quick-input-list .monaco-list-row[data-index="0"] .quick-input-list-entry.quick-input-list-separator-border {
	border-top-style: none;
}

.quick-input-list .quick-input-list-label {
	overflow: hidden;
	display: flex;
	height: 100%;
	flex: 1;
}

.quick-input-list .quick-input-list-checkbox {
	align-self: center;
	margin: 0;
}

.quick-input-list .quick-input-list-rows {
	overflow: hidden;
	text-overflow: ellipsis;
	display: flex;
	flex-direction: column;
	height: 100%;
	flex: 1;
	margin-left: 5px;
}

.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-rows {
	margin-left: 10px;
}

.quick-input-widget .quick-input-list .quick-input-list-checkbox {
	display: none;
}
.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-checkbox {
	display: inline;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row {
	display: flex;
	align-items: center;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label,
.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label .monaco-icon-label-container > .monaco-icon-name-container {
	flex: 1; /* make sure the icon label grows within the row */
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .codicon[class*='codicon-'] {
	vertical-align: text-bottom;
}

.quick-input-list .quick-input-list-rows .monaco-highlighted-label span {
	opacity: 1;
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-keybinding {
	margin-right: 8px; /* separate from the separator label or scrollbar if any */
}

.quick-input-list .quick-input-list-label-meta {
	opacity: 0.7;
	line-height: normal;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-list .monaco-highlighted-label .highlight {
	font-weight: bold;
}

.quick-input-list .quick-input-list-entry .quick-input-list-separator {
	margin-right: 8px; /* separate from keybindings or actions */
}

.quick-input-list .quick-input-list-entry-action-bar {
	display: flex;
	flex: 0;
	overflow: visible;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label {
	/*
	 * By default, actions in the quick input action bar are hidden
	 * until hovered over them or selected.
	 */
	display: none;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label.codicon {
	margin-right: 4px;
	padding: 0px 2px 2px 2px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-top: 1px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-right: 4px; /* separate from scrollbar */
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-action-bar .action-label.always-visible,
.quick-input-list .quick-input-list-entry:hover .quick-input-list-entry-action-bar .action-label,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry-action-bar .action-label {
	display: flex;
}

/* focused items in quick pick */
.quick-input-list .monaco-list-row.focused .monaco-keybinding-key,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry .quick-input-list-separator {
	color: inherit
}
.quick-input-list .monaco-list-row.focused .monaco-keybinding-key {
	background: none;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-keybinding {
	display: flex;
	align-items: center;
	line-height: 10px;
}

.monaco-keybinding > .monaco-keybinding-key {
	display: inline-block;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	vertical-align: middle;
	font-size: 11px;
	padding: 3px 5px;
	margin: 0 2px;
}

.monaco-keybinding > .monaco-keybinding-key:first-child {
	margin-left: 0;
}

.monaco-keybinding > .monaco-keybinding-key:last-child {
	margin-right: 0;
}

.monaco-keybinding > .monaco-keybinding-key-separator {
	display: inline-block;
}

.monaco-keybinding > .monaco-keybinding-key-chord-separator {
	width: 6px;
}
</style><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.monaco-editor .accessibilityHelpWidget { background-color: #f3f3f3; }
.monaco-editor .accessibilityHelpWidget { color: #616161; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px rgba(0, 0, 0, 0.16); }
.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #fffffe; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #2e2e2e; }
.monaco-editor .margin { background-color: #fffffe; }
.monaco-editor .rangeHighlight { background-color: rgba(253, 255, 0, 0.2); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .mtkw { color: #bbbbbb !important; }
.monaco-editor .mtkz { color: #bbbbbb !important; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #b9b9b9; }
.monaco-editor .monaco-editor-overlaymessage .anchor.below { border-top-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .anchor.top { border-bottom-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { border: 1px solid #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { background-color: #d6ecf2; }

		.monaco-editor .contentWidgets .codicon.codicon-light-bulb {
			color: #ddb100;
			background-color: rgba(255, 255, 254, 0.7);
		}

		.monaco-editor .contentWidgets .codicon.codicon-lightbulb-autofix {
			color: #007acc;
			background-color: rgba(255, 255, 254, 0.7);
		}
.monaco-editor .codelens-decoration { color: #919191; }
.monaco-editor .codelens-decoration .codicon { color: #919191; }
.monaco-editor .codelens-decoration > a:hover { color: #0000ff !important; }
.monaco-editor .codelens-decoration > a:hover .codicon { color: #0000ff !important; }
.monaco-editor .line-numbers { color: #cccccc; }
.monaco-editor .line-numbers.active-line-number { color: #0b216f; }
.monaco-editor .view-overlays .current-line { background-color: #fffeeb; }
.monaco-editor .margin-view-overlays .current-line-margin { background-color: #fffeeb; border: none; }

			.monaco-scrollable-element > .shadow.top {
				box-shadow: #dddddd 0 6px 6px -6px inset;
			}

			.monaco-scrollable-element > .shadow.left {
				box-shadow: #dddddd 6px 0 6px -6px inset;
			}

			.monaco-scrollable-element > .shadow.top.left {
				box-shadow: #dddddd 6px 6px 6px -6px inset;
			}
		

			.monaco-scrollable-element > .scrollbar > .slider {
				background: rgba(100, 100, 100, 0.4);
			}
		

			.monaco-scrollable-element > .scrollbar > .slider:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-scrollable-element > .scrollbar > .slider.active {
				background: rgba(0, 0, 0, 0.6);
			}
		
.monaco-editor .lines-content .core-guide-indent { box-shadow: 1px 0 0 0 #bbbbbb inset; }
.monaco-editor .lines-content .core-guide-indent-active { box-shadow: 1px 0 0 0 #cccccc inset; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.2); }
.monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(0, 0, 0, 0.3); }
.monaco-editor .minimap-shadow-visible { box-shadow: #dddddd -6px 0 6px -6px inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .scroll-decoration { box-shadow: #dddddd 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #aad6f8; }
.monaco-editor .selected-text { background-color: rgba(170, 214, 248, 0.5); }
.monaco-editor .cursors-layer .cursor { background-color: #666666; border-color: #666666; color: #999999; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor.showDeprecated .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #2e2e2e}
.monaco-editor .reference-zone-widget .ref-tree .referenceMatch .highlight { background-color: rgba(234, 92, 0, 0.3); }
.monaco-editor .reference-zone-widget .preview .reference-decoration { background-color: rgba(245, 216, 2, 0.87); }
.monaco-editor .reference-zone-widget .ref-tree { background-color: #f3f3f3; }
.monaco-editor .reference-zone-widget .ref-tree { color: #646465; }
.monaco-editor .reference-zone-widget .ref-tree .reference-file { color: #1e1e1e; }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { background-color: rgba(51, 153, 255, 0.2); }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { color: #6c6c6c !important; }
.monaco-editor .reference-zone-widget .preview .monaco-editor .monaco-editor-background,.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.ime-input {	background-color: #f2f8fc;}
.monaco-editor .reference-zone-widget .preview .monaco-editor .margin {	background-color: #f2f8fc;}
.monaco-editor .goto-definition-link { color: #0000ff !important; }

			.monaco-editor .zone-widget .codicon.codicon-error,
			.markers-panel .marker-icon.codicon.codicon-error,
			.text-search-provider-messages .providerMessage .codicon.codicon-error,
			.extensions-viewlet > .extensions .codicon.codicon-error {
				color: #e51400;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-warning,
			.markers-panel .marker-icon.codicon.codicon-warning,
			.extensions-viewlet > .extensions .codicon.codicon-warning,
			.extension-editor .codicon.codicon-warning,
			.text-search-provider-messages .providerMessage .codicon.codicon-warning,
			.preferences-editor .codicon.codicon-warning {
				color: #bf8803;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-info,
			.markers-panel .marker-icon.codicon.codicon-info,
			.extensions-viewlet > .extensions .codicon.codicon-info,
			.text-search-provider-messages .providerMessage .codicon.codicon-info,
			.extension-editor .codicon.codicon-info {
				color: #1a85ff;
			}
		
.monaco-editor .marker-widget a.code-link span { color: #006ab1; }
.monaco-editor .marker-widget a.code-link span:hover { color: #006ab1; }
.monaco-hover .hover-contents a.code-link span { color: #006ab1; }
.monaco-hover .hover-contents a.code-link span:hover { color: #006ab1; }
.monaco-editor .snippet-placeholder { background-color: rgba(10, 50, 100, 0.2); outline-color: transparent; }
.monaco-editor .finish-snippet-placeholder { background-color: transparent; outline-color: rgba(10, 50, 100, 0.5); }
.codicon.codicon-symbol-array { color: #616161; }
.codicon.codicon-symbol-boolean { color: #616161; }
.codicon.codicon-symbol-class { color: #d67e00; }
.codicon.codicon-symbol-method { color: #652d90; }
.codicon.codicon-symbol-color { color: #616161; }
.codicon.codicon-symbol-constant { color: #616161; }
.codicon.codicon-symbol-constructor { color: #652d90; }

			.codicon.codicon-symbol-value,.codicon.codicon-symbol-enum { color: #d67e00; }
.codicon.codicon-symbol-enum-member { color: #007acc; }
.codicon.codicon-symbol-event { color: #d67e00; }
.codicon.codicon-symbol-field { color: #007acc; }
.codicon.codicon-symbol-file { color: #616161; }
.codicon.codicon-symbol-folder { color: #616161; }
.codicon.codicon-symbol-function { color: #652d90; }
.codicon.codicon-symbol-interface { color: #007acc; }
.codicon.codicon-symbol-key { color: #616161; }
.codicon.codicon-symbol-keyword { color: #616161; }
.codicon.codicon-symbol-module { color: #616161; }
.codicon.codicon-symbol-namespace { color: #616161; }
.codicon.codicon-symbol-null { color: #616161; }
.codicon.codicon-symbol-number { color: #616161; }
.codicon.codicon-symbol-object { color: #616161; }
.codicon.codicon-symbol-operator { color: #616161; }
.codicon.codicon-symbol-package { color: #616161; }
.codicon.codicon-symbol-property { color: #616161; }
.codicon.codicon-symbol-reference { color: #616161; }
.codicon.codicon-symbol-snippet { color: #616161; }
.codicon.codicon-symbol-string { color: #616161; }
.codicon.codicon-symbol-struct { color: #616161; }
.codicon.codicon-symbol-text { color: #616161; }
.codicon.codicon-symbol-type-parameter { color: #616161; }
.codicon.codicon-symbol-unit { color: #616161; }
.codicon.codicon-symbol-variable { color: #007acc; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight { color: #0066bf; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused .monaco-highlighted-label .highlight { color: #96d8fd; }
.monaco-editor .suggest-widget, .monaco-editor .suggest-details { color: #2e2e2e; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused { color: #ffffff; }
.monaco-editor .suggest-details a { color: #006ab1; }
.monaco-editor .suggest-details a:hover { color: #006ab1; }
.monaco-editor .suggest-details code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .ghost-text-decoration { opacity: 0.467 !important; color: #000000 !important; }
.monaco-editor .ghost-text-decoration-preview { color: rgba(0, 0, 0, 0.47) !important; }
.monaco-editor .suggest-preview-text .ghost-text { opacity: 0.467 !important; color: #000000 !important; }
.monaco-editor .hoverHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .monaco-hover { background-color: #f3f3f3; }
.monaco-editor .monaco-hover { border: 1px solid #c8c8c8; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover a { color: #006ab1; }
.monaco-editor .monaco-hover a:hover { color: #006ab1; }
.monaco-editor .monaco-hover { color: #616161; }
.monaco-editor .monaco-hover .hover-row .actions { background-color: #e7e7e7; }
.monaco-editor .monaco-hover code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .findOptionsWidget { background-color: #f3f3f3; }
.monaco-editor .findOptionsWidget { color: #616161; }
.monaco-editor .findOptionsWidget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .folded-background { background-color: rgba(170, 214, 248, 0.3); }

		.monaco-editor .cldr.codicon.codicon-folding-expanded,
		.monaco-editor .cldr.codicon.codicon-folding-collapsed {
			color: #424242 !important;
		}
		
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #b9b9b9; }
.monaco-editor .tokens-inspect-widget { border: 1px solid #c8c8c8; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #c8c8c8; }
.monaco-editor .tokens-inspect-widget { background-color: #f3f3f3; }
.monaco-editor .tokens-inspect-widget { color: #616161; }
.monaco-editor .linked-editing-decoration { background: rgba(255, 0, 0, 0.3); border-left-color: rgba(255, 0, 0, 0.3); }
.monaco-editor .detected-link-active { color: #0000ff !important; }
.monaco-editor .parameter-hints-widget { border: 1px solid #c8c8c8; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #f3f3f3; }
.monaco-editor .parameter-hints-widget a { color: #006ab1; }
.monaco-editor .parameter-hints-widget a:hover { color: #006ab1; }
.monaco-editor .parameter-hints-widget { color: #616161; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .parameter-hints-widget .parameter.active { color: #0066bf}
.monaco-editor .focused .selectionHighlight { background-color: rgba(213, 235, 252, 0.6); }
.monaco-editor .selectionHighlight { background-color: rgba(213, 235, 252, 0.3); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.25); }
.monaco-editor .wordHighlightStrong { background-color: rgba(14, 99, 156, 0.25); }
.monaco-diff-editor .diff-review-line-number { color: #cccccc; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #dddddd 0 -6px 6px -6px inset; }
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(160, 245, 180, 0.13); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(160, 245, 180, 0.13); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(160, 245, 180, 0.13); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(249, 215, 220, 0.13); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(249, 215, 220, 0.13); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(249, 215, 220, 0.13); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #dddddd; }

			.monaco-diff-editor .diffViewport {
				background: rgba(100, 100, 100, 0.4);
			}
		

			.monaco-diff-editor .diffViewport:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-diff-editor .diffViewport:active {
				background: rgba(0, 0, 0, 0.6);
			}
		

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	

.mtk1 { color: #2e2e2e; }
.mtk2 { color: #ffffff; }
.mtk3 { color: #008080; }
.mtk4 { color: #dd1144; }
.mtk5 { color: #0086b3; }
.mtk6 { color: #aa0000; }
.mtk7 { color: #009999; }
.mtk8 { color: #999988; }
.mtk9 { color: #999999; }
.mtk10 { color: #800080; }
.mtk11 { color: #990073; }
.mtk12 { color: #666666; }
.mtk13 { color: #000080; }
.mtk14 { color: #445588; }
.mtk15 { color: #e3d2d2; }
.mtk16 { color: #863b00; }
.mtk17 { color: #000000; }
.mtk18 { color: #ffdddd; }
.mtk19 { color: #ddffdd; }
.mtk20 { color: #808080; }
.mtk21 { color: #eaf2f5; }
.mtk22 { color: #4183c4; }
.mtk23 { color: #800000; }
.mtk24 { color: #e00000; }
.mtk25 { color: #3030c0; }
.mtk26 { color: #009926; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }</style><style type="text/css" media="screen">
		.monaco-editor .codelens-decoration._ee1f61 { line-height: 19px; font-size: 12px; padding-right: 6px; font-feature-settings: var(--codelens-font-features_ee1f61) }
		.monaco-editor .codelens-decoration._ee1f61 span.codicon { line-height: 19px; font-size: 12px; }
		</style><script charset="utf-8" src="./README_files/1074.713ced63.chunk.js"></script><script charset="utf-8" src="./README_files/1035.a1fda1dc.chunk.js"></script><script charset="utf-8" src="./README_files/1036.f7703651.chunk.js"></script><script charset="utf-8" src="./README_files/173.28e96ac2.chunk.js"></script><script charset="utf-8" src="./README_files/vendors-globalSearch-top_nav.39428307.chunk.js"></script><script charset="utf-8" src="./README_files/vendors-top_nav.780880ca.chunk.js"></script><script charset="utf-8" src="./README_files/top_nav.b93fb456.chunk.js"></script></head>

<body class="ui-indigo tab-width-8 gl-browser-chrome gl-platform-linux page-initialised" data-find-file="/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/find_file/main" data-group="manish" data-namespace-id="60082598" data-page="projects:blob:edit" data-page-type-id="main/README.md" data-project="ipl-data-set-analytics" data-project-id="40954144">

<script nonce="">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isChrome":true,"isLinux":true};


//]]>
</script>



<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="gl-sr-only gl-accessibility" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md#content-body">Skip to content</a>
<div class="container-fluid">
<div class="header-content js-header-content">
<div class="title-container hide-when-top-nav-responsive-open gl-transition-medium gl-display-flex gl-align-items-stretch gl-pt-0 gl-mr-3">
<div class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" class="has-tooltip" data-track-label="main_navigation" data-track-action="click_gitlab_logo_link" data-track-property="navigation" href="https://gitlab.com/"><svg class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z" fill="#E24329"></path>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z" fill="#FC6D26"></path>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z" fill="#FCA326"></path>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z" fill="#FC6D26"></path>
</svg>

</a></div>
<div class="gl-display-flex gl-align-items-center">
</div>
<div class="gl-display-none gl-sm-display-block">
<ul class="nav navbar-sub-nav"><li class="nav-item b-nav-dropdown dropdown gl-new-dropdown" data-qa-selector="navbar_dropdown" data-qa-title="Menu" id="__BVID__17"><a role="button" aria-haspopup="true" aria-expanded="false" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md#" target="_self" class="nav-link dropdown-toggle top-nav-toggle js-top-nav-dropdown-toggle gl-px-3! dropdown-toggle-no-caret" id="__BVID__17__BV_toggle_"><svg data-testid="hamburger-icon" role="img" aria-hidden="true" class="gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#hamburger"></use></svg> <!----></a><ul tabindex="-1" class="dropdown-menu gl-mt-3! gl-max-w-none! gl-max-h-none! gl-sm-w-auto! js-top-nav-dropdown-menu" aria-labelledby="__BVID__17__BV_toggle_"> <li role="presentation"><form tabindex="-1" class="b-dropdown-form gl-p-0"><div class="gl-display-flex gl-align-items-stretch"><div data-testid="menu-sidebar" class="gl-w-grid-size-30 gl-flex-shrink-0 gl-bg-gray-10 gl-p-3"><div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column"><div data-testid="menu-section" class=""><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block">
        Switch to
      </strong><button aria-label="Projects" data-track-label="projects_dropdown" data-track-action="click_dropdown" type="button" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary qa-projects-dropdown gl-shadow-none! gl-font-weight-bold! active gl-mt-1" href="" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="project-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#project"></use></svg> 
      Projects
      <svg data-testid="chevron-right-icon" role="img" aria-hidden="true" class="gl-ml-auto gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-right"></use></svg></span></span></button><button aria-label="Groups" data-track-label="groups_dropdown" data-track-action="click_dropdown" type="button" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary qa-groups-dropdown gl-mt-1" href="" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="group-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#group"></use></svg> 
      Groups
      <svg data-testid="chevron-right-icon" role="img" aria-hidden="true" class="gl-ml-auto gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-right"></use></svg></span></span></button><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block gl-pt-3!">
        Explore
      </strong><a aria-label="Milestones" data-qa-selector="milestones_link" data-track-label="menu_milestones" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/milestones" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="clock-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#clock"></use></svg> 
      Milestones
      <!----></span></span></a><a aria-label="Snippets" data-qa-selector="snippets_link" data-track-label="menu_snippets" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/snippets" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="snippet-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#snippet"></use></svg> 
      Snippets
      <!----></span></span></a><a aria-label="Activity" data-qa-selector="activity_link" data-track-label="menu_activity" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/activity" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="history-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#history"></use></svg> 
      Activity
      <!----></span></span></a><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block gl-pt-3!">
        Your dashboards
      </strong><a aria-label="Environments" data-qa-selector="environment_link" data-track-label="menu_environments" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/-/operations/environments" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="environment-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#environment"></use></svg> 
      Environments
      <!----></span></span></a><a aria-label="Operations" data-qa-selector="operations_link" data-track-label="menu_operations" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/-/operations" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="cloud-gear-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#cloud-gear"></use></svg> 
      Operations
      <!----></span></span></a><a aria-label="Security" data-qa-selector="security_link" data-track-label="menu_security" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/-/security/dashboard" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="shield-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#shield"></use></svg> 
      Security
      <!----></span></span></a></div></div></div> <div data-testid="menu-subview" data-qa-selector="menu_subview_container" class="gl-w-grid-size-40 gl-overflow-hidden gl-p-3"><div class="gl-h-full gl-w-full"><div class="top-nav-container-view gl-display-flex gl-flex-direction-column"><div data-testid="frequent-items-container" class="frequent-items-dropdown-container gl-w-auto"><div class="frequent-items-dropdown-content gl-w-full! gl-pt-0!"><div class="gl-display-flex gl-flex-direction-column gl-flex-align-items-stretch gl-h-full"><div class="search-input-container" data-testid="frequent-items-search-input"><div class="gl-search-box-by-type"><svg data-testid="search-icon" role="img" aria-hidden="true" class="gl-search-box-by-type-search-icon gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg> <input type="search" placeholder="Search your projects" class="gl-form-input gl-search-box-by-type-input form-control" aria-label="Search your projects" id="__BVID__63"> <div class="gl-search-box-by-type-right-icons"><!----> <!----></div></div></div> <!----> <div data-testid="header" class="section-header">
    Frequently visited
  </div> <div class="frequent-items-list-container"><ul data-testid="frequent-items-list" class="list-unstyled"><li class="frequent-items-list-item-container"><a href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics" class="btn gl-text-left gl-justify-content-start! btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><div class="gl-float-left gl-mr-3 gl-avatar gl-avatar-identicon gl-avatar-s32 gl-avatar-identicon-bg1" aria-hidden="true">
  I
</div> <div data-testid="frequent-items-item-metadata-container" class="frequent-items-item-metadata-container"><div data-testid="frequent-items-item-title" title="IPL data set analytics" class="frequent-items-item-title">IPL data set analytics</div> <div data-testid="frequent-items-item-namespace" title="mountblue / Cohort 22 Python / Manish / IPL data set analytics" class="frequent-items-item-namespace">
        mountblue / ... / Manish
      </div></div></span></a></li><li class="frequent-items-list-item-container"><a href="https://gitlab.com/mountblue/cohort-22-python/manish/analytics-on-un-population" class="btn gl-text-left gl-justify-content-start! btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><div class="gl-float-left gl-mr-3 gl-avatar gl-avatar-identicon gl-avatar-s32 gl-avatar-identicon-bg5" aria-hidden="true">
  A
</div> <div data-testid="frequent-items-item-metadata-container" class="frequent-items-item-metadata-container"><div data-testid="frequent-items-item-title" title="Analytics on UN Population" class="frequent-items-item-title">Analytics on UN Population</div> <div data-testid="frequent-items-item-namespace" title="mountblue / Cohort 22 Python / Manish / Analytics on UN Population" class="frequent-items-item-namespace">
        mountblue / ... / Manish
      </div></div></span></a></li><li class="frequent-items-list-item-container"><a href="https://gitlab.com/mountblue/cohort-22-python/manish/life-skills-repo" class="btn gl-text-left gl-justify-content-start! btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><div class="gl-float-left gl-mr-3 gl-avatar gl-avatar-identicon gl-avatar-s32 gl-avatar-identicon-bg2" aria-hidden="true">
  L
</div> <div data-testid="frequent-items-item-metadata-container" class="frequent-items-item-metadata-container"><div data-testid="frequent-items-item-title" title="Life Skills repo" class="frequent-items-item-title">Life Skills repo</div> <div data-testid="frequent-items-item-namespace" title="mountblue / Cohort 22 Python / Manish / Life Skills repo" class="frequent-items-item-namespace">
        mountblue / ... / Manish
      </div></div></span></a></li><li class="frequent-items-list-item-container"><a href="https://gitlab.com/mountblue/cohort-22-python/manish/company-master-maharashtra" class="btn gl-text-left gl-justify-content-start! btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><div class="gl-float-left gl-mr-3 gl-avatar gl-avatar-identicon gl-avatar-s32 gl-avatar-identicon-bg2" aria-hidden="true">
  C
</div> <div data-testid="frequent-items-item-metadata-container" class="frequent-items-item-metadata-container"><div data-testid="frequent-items-item-title" title="Company Master - Maharashtra" class="frequent-items-item-title">Company Master - Maharashtra</div> <div data-testid="frequent-items-item-namespace" title="mountblue / Cohort 22 Python / Manish / Company Master - Maharashtra" class="frequent-items-item-namespace">
        mountblue / ... / Manish
      </div></div></span></a></li><li class="frequent-items-list-item-container"><a href="https://gitlab.com/manish152/life-skills" class="btn gl-text-left gl-justify-content-start! btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><div class="gl-float-left gl-mr-3 gl-avatar gl-avatar-identicon gl-avatar-s32 gl-avatar-identicon-bg4" aria-hidden="true">
  L
</div> <div data-testid="frequent-items-item-metadata-container" class="frequent-items-item-metadata-container"><div data-testid="frequent-items-item-title" title="Life Skills" class="frequent-items-item-title">Life Skills</div> <div data-testid="frequent-items-item-namespace" title="Manish / Life Skills" class="frequent-items-item-namespace">
        Manish
      </div></div></span></a></li></ul></div></div></div></div> <div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column gl-mt-auto"><div data-testid="menu-section" class="gl-pt-3 gl-border-1 gl-border-t-solid gl-border-gray-50"><a aria-label="View all projects" data-qa-selector="menu_item_link" data-qa-title="View all projects" data-track-label="menu_view_all_projects" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/projects" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><!----> 
      View all projects
      <!----></span></span></a></div></div></div></div></div></div></form></li></ul></li></ul>
<div class="hidden">
<a class="dashboard-shortcuts-projects" href="https://gitlab.com/dashboard/projects">Projects
</a><a class="dashboard-shortcuts-groups" href="https://gitlab.com/dashboard/groups">Groups
</a><a class="dashboard-shortcuts-milestones" href="https://gitlab.com/dashboard/milestones">Milestones
</a><a class="dashboard-shortcuts-snippets" href="https://gitlab.com/dashboard/snippets">Snippets
</a><a class="dashboard-shortcuts-activity" href="https://gitlab.com/dashboard/activity">Activity
</a></div>

</div>
</div>
<div class="navbar-collapse gl-transition-medium collapse gl-mr-auto global-search-container hide-when-top-nav-responsive-open">
<ul class="nav navbar-nav gl-w-full gl-align-items-center">
<li class="nav-item header-search-new gl-display-none gl-lg-display-block gl-w-full">
<div class="header-search is-not-active gl-relative gl-w-full" data-autocomplete-path="/search/autocomplete" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-search-context="{&quot;group&quot;:{&quot;id&quot;:60082598,&quot;name&quot;:&quot;Manish&quot;,&quot;full_name&quot;:&quot;mountblue / Cohort 22 Python / Manish&quot;},&quot;group_metadata&quot;:{&quot;issues_path&quot;:&quot;/groups/mountblue/cohort-22-python/manish/-/issues&quot;,&quot;mr_path&quot;:&quot;/groups/mountblue/cohort-22-python/manish/-/merge_requests&quot;},&quot;project&quot;:{&quot;id&quot;:40954144,&quot;name&quot;:&quot;IPL data set analytics&quot;},&quot;project_metadata&quot;:{&quot;issues_path&quot;:&quot;/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues&quot;,&quot;mr_path&quot;:&quot;/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/merge_requests&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;main&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}" data-search-path="/search" id="js-header-search">
<form action="https://gitlab.com/search" accept-charset="UTF-8" method="get"><div class="gl-search-box-by-type">
<svg class="s16 gl-search-box-by-type-search-icon gl-icon" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg>
<input autocomplete="off" class="form-control gl-form-input gl-search-box-by-type-input" data-qa-selector="search_box" id="search" name="search" placeholder="Search GitLab" type="text">
</div>
<input type="hidden" name="group_id" id="group_id" value="60082598" autocomplete="off">
<input type="hidden" name="project_id" id="project_id" value="40954144" autocomplete="off">
<input type="hidden" name="scope" id="scope" autocomplete="off">
<input type="hidden" name="search_code" id="search_code" value="true" autocomplete="off">
<input type="hidden" name="snippets" id="snippets" autocomplete="off">
<input type="hidden" name="repository_ref" id="repository_ref" value="main" autocomplete="off">
<input type="hidden" name="nav_source" id="nav_source" value="navbar" autocomplete="off">
<kbd class="gl-absolute gl-right-3 gl-top-0 keyboard-shortcut-helper gl-z-index-1 has-tooltip" data-html="true" data-placement="bottom" title="Use the shortcut key &lt;kbd&gt;/&lt;/kbd&gt; to start a search">
/
</kbd>
</form></div>

</li>
<li class="nav-item d-none d-sm-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="https://gitlab.com/search?project_id=40954144"><svg class="s16" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg>
</a></li>
</ul>
</div>
<div class="navbar-collapse gl-transition-medium collapse">
<ul class="nav navbar-nav gl-w-full gl-align-items-center gl-justify-content-end">
<li class="header-new gl-flex-grow-1 gl-flex-shrink-1 dropdown gl-display-none gl-sm-display-block gl-white-space-nowrap gl-text-right" data-track-action="click_dropdown" data-track-label="new_dropdown">
<a class="header-new-dropdown-toggle has-tooltip gl-display-flex" id="js-onboarding-new-project-link" title="Create new..." ref="tooltip" aria-label="Create new..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" data-qa-selector="new_menu_toggle" href="https://gitlab.com/projects/new"><svg class="s16" data-testid="plus-square-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#plus-square"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right dropdown-extended-height">
<ul>
<li class="dropdown-bold-header">
This project
</li>
<li><a data-track-action="click_link_new_issue" data-track-label="plus_menu_dropdown" data-qa-selector="new_issue_link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues/new">New issue</a></li>
<li><a data-track-action="click_link_new_mr" data-track-label="plus_menu_dropdown" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/merge_requests/new">New merge request</a></li>
<li><a data-track-action="click_link_new_snippet_project" data-track-label="plus_menu_dropdown" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/snippets/new">New snippet</a></li>
<li><a data-track-action="click_link_invite_members" data-track-label="plus_menu_dropdown" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/project_members">Invite members <gl-emoji title="handshake" data-name="handshake" data-unicode-version="9.0" aria-hidden="true" class="gl-font-base gl-vertical-align-baseline">🤝</gl-emoji></a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">
GitLab
</li>
<li><a data-track-action="click_link_new_project" data-track-label="plus_menu_dropdown" data-qa-selector="global_new_project_link" href="https://gitlab.com/projects/new">New project/repository</a></li>
<li><a data-track-action="click_link_new_group" data-track-label="plus_menu_dropdown" data-qa-selector="global_new_group_link" href="https://gitlab.com/groups/new">New group</a></li>
<li><a data-track-action="click_link_new_snippet_parent" data-track-label="plus_menu_dropdown" data-qa-selector="global_new_snippet_link" href="https://gitlab.com/-/snippets/new">New snippet</a></li>
</ul>
</div>
</li>

<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues js-prefetch-document" aria-label="Issues" data-qa-selector="issues_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-action="click_issues_link" data-track-property="navigation" data-container="body" href="https://gitlab.com/dashboard/issues?assignee_username=md_manish"><svg class="s16" data-testid="issues-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#issues"></use></svg>
<span aria-label="9 assigned issues" class="gl-badge badge badge-pill badge-success sm gl-ml-n2 ">9
</span></a></li><li class="user-counter dropdown"><a class="dashboard-shortcuts-merge_requests has-tooltip" title="Merge requests" aria-label="Merge requests" data-qa-selector="merge_requests_shortcut_button" data-toggle="dropdown" data-placement="bottom" data-track-label="main_navigation" data-track-action="click_merge_link" data-track-property="navigation" data-container="body" href="https://gitlab.com/dashboard/merge_requests?assignee_username=md_manish"><svg class="s16" data-testid="git-merge-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#git-merge"></use></svg>
<span aria-label="0 merge requests" class="gl-badge badge badge-pill badge-warning sm js-merge-requests-count gl-ml-n2 gl-display-none">0
</span><svg class="s16 caret-down gl-mx-0!" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="dropdown-header">
Merge requests
</li>
<li>
<a class="gl-display-flex! gl-align-items-center js-prefetch-document" href="https://gitlab.com/dashboard/merge_requests?assignee_username=md_manish">Assigned to you
<span class="gl-badge badge badge-pill badge-neutral sm js-assigned-mr-count gl-ml-auto">0
</span></a></li>
<li>
<a class="dashboard-shortcuts-review_requests gl-display-flex! gl-align-items-center js-prefetch-document" href="https://gitlab.com/dashboard/merge_requests?reviewer_username=md_manish">Review requests for you
<span class="gl-badge badge badge-pill badge-neutral sm js-reviewer-mr-count gl-ml-auto">0
</span></a></li>
</ul>
</div>
</li><li class="user-counter"><a title="To-Do List" aria-label="To-Do List" class="shortcuts-todos js-prefetch-document" data-qa-selector="todos_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-action="click_to_do_link" data-track-property="navigation" data-container="body" href="https://gitlab.com/dashboard/todos"><svg class="s16" data-testid="todo-done-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#todo-done"></use></svg>
<span aria-label="Todos count" class="gl-badge badge badge-pill badge-info sm js-todos-count gl-ml-n2 hidden">0
</span></a></li><li class="nav-item header-help dropdown d-none d-md-block with-notifications" data-track-action="click_question_mark_link" data-track-experiment="cross_stage_fdm" data-track-label="main_navigation" data-track-property="navigation">
<a class="header-help-dropdown-toggle gl-relative" data-toggle="dropdown" href="https://gitlab.com/help"><span class="gl-sr-only">
Help
</span>
<svg class="s16" data-testid="question-o-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#question-o"></use></svg>
<span class="notification-dot rounded-circle gl-absolute"></span>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li>

</li>

<li>
<button class="gl-justify-content-space-between gl-align-items-center js-whats-new-trigger gl-display-flex!" type="button">
What's new
<span class="gl-badge badge badge-pill badge-muted sm js-whats-new-notification-count">7</span>
</button>
</li>

<li>
<a href="https://gitlab.com/help">Help</a>
</li>
<li>
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li>
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-action="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li>
<button class="js-shortcuts-modal-trigger" type="button">
Keyboard shortcuts
<kbd aria-hidden="true" class="flat float-right">?</kbd>
</button>
</li>
<li class="divider"></li>
<li>
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li>
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>

</li>

<li>
<a href="https://next.gitlab.com/">Switch to GitLab Next</a>
</li>
</ul>

</div>
</li>
<li class="nav-item header-user js-nav-user-dropdown dropdown" data-qa-selector="user_menu" data-testid="user-menu" data-track-action="click_dropdown" data-track-label="profile_dropdown" data-track-value="">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="https://gitlab.com/md_manish"><img srcset="https://secure.gravatar.com/avatar/339a5a437f934e7f4f79a776a044609a?s=48&amp;d=identicon 1x, https://secure.gravatar.com/avatar/339a5a437f934e7f4f79a776a044609a?s=48&amp;d=identicon 2x" alt="Md Manishurrahman" class="gl-avatar gl-avatar-s24 header-user-avatar gl-avatar-circle" height="24" width="24" loading="lazy" data-qa-selector="user_avatar_content" src="./README_files/339a5a437f934e7f4f79a776a044609a">


<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="current-user">
<a class="gl-line-height-20!" data-user="md_manish" data-testid="user-profile-link" data-qa-selector="user_profile_link" href="https://gitlab.com/md_manish"><div class="gl-font-weight-bold">
Md Manishurrahman
</div>
@md_manish

</a></li>
<li class="divider"></li>
<li>
<button class="gl-button btn btn-link menu-item js-set-status-modal-trigger" type="button">
Set status
</button>
</li>
<li>
<a class="trial-link" href="https://gitlab.com/-/trial_registrations/new?glm_content=top-right-dropdown&amp;glm_source=gitlab.com">
Start an Ultimate trial
<gl-emoji title="rocket" data-name="rocket" data-unicode-version="6.0">🚀</gl-emoji>
</a>
</li>
<li>
<a data-qa-selector="edit_profile_link" href="https://gitlab.com/-/profile">Edit profile</a>
</li>
<li>
<a href="https://gitlab.com/-/profile/preferences">Preferences</a>
</li>

<li class="divider d-md-none"></li>
<li class="d-md-none">
<a href="https://gitlab.com/help">Help</a>
</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-action="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>

</li>

<li class="d-md-none">
<a href="https://next.gitlab.com/">Switch to GitLab Next</a>
</li>
<li class="divider"></li>
<li>
<a class="sign-out-link" data-qa-selector="sign_out_link" rel="nofollow" data-method="post" href="https://gitlab.com/users/sign_out">Sign out</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none gl-border-none!" data-qa-selector="mobile_navbar_button" data-testid="top-nav-responsive-toggle" type="button">
<span class="sr-only">Toggle navigation</span>
<span class="more-icon gl-px-3 gl-font-sm gl-font-weight-bold">
<span class="gl-pr-2">Menu</span>
<svg class="s16" data-testid="hamburger-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#hamburger"></use></svg>
</span>
<svg class="s12 close-icon" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<div data-version-digest="64783b31865d39a375be1a54f8aecd26aa00de65e30cc7cef0f3fd8b49b4ac5b" id="whats-new-app"></div>
<div class="js-set-status-modal-wrapper" data-current-emoji="" data-current-message="" data-default-emoji="speech_balloon"></div>

<div class="layout-page hide-when-top-nav-responsive-open page-with-contextual-sidebar">
<aside aria-label="Project navigation" class="nav-sidebar" data-track-action="render" data-track-label="projects_side_navigation" data-track-property="projects_side_navigation">
<div class="nav-sidebar-inner-scroll" style="overflow-y: scroll;">
<ul class="sidebar-top-level-items" data-qa-selector="project_sidebar">
<li data-track-label="scope_menu" data-container="body" data-placement="right" class="context-header has-tooltip" title="IPL data set analytics"><a aria-label="IPL data set analytics" class="shortcuts-project rspec-project-link gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project scope" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics"><span class="avatar-container rect-avatar s32 project_avatar">
<span class="avatar avatar-tile s32 identicon bg1">I</span>
</span>
<span class="sidebar-context-title">
IPL data set analytics
</span>
</a></li>
<li data-track-label="project_information_menu" class="home"><a aria-label="Project information" class="shortcuts-project-information has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project information" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/activity"><span class="nav-icon-container">
<svg class="s16" data-testid="project-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#project"></use></svg>
</span>
<span class="nav-item-name">
Project information
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Project information
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="activity" class=""><a aria-label="Activity" class="shortcuts-project-activity gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Activity" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/activity"><span>
Activity
</span>
</a></li><li data-track-label="labels" class=""><a aria-label="Labels" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Labels" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/labels"><span>
Labels
</span>
</a></li><li data-track-label="members" class=""><a aria-label="Members" id="js-onboarding-members-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Members" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/project_members"><span>
Members
</span>
</a></li>
</ul>

</li><li data-track-label="repository_menu" class="active"><a aria-label="Repository" class="shortcuts-tree has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Repository" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/tree/main"><span class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#doc-text"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-repo-link">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Repository
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="files" class="active"><a aria-label="Files" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Files" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/tree/main"><span>
Files
</span>
</a></li><li data-track-label="commits" class=""><a aria-label="Commits" id="js-onboarding-commits-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Commits" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/commits/main"><span>
Commits
</span>
</a></li><li data-track-label="branches" class=""><a aria-label="Branches" id="js-onboarding-branches-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Branches" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/branches"><span>
Branches
</span>
</a></li><li data-track-label="tags" class=""><a aria-label="Tags" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Tags" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/tags"><span>
Tags
</span>
</a></li><li data-track-label="contributors" class=""><a aria-label="Contributors" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Contributors" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/graphs/main"><span>
Contributors
</span>
</a></li><li data-track-label="graphs" class=""><a aria-label="Graph" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Graph" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/network/main"><span>
Graph
</span>
</a></li><li data-track-label="compare" class=""><a aria-label="Compare" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Compare" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/compare?from=main&amp;to=main"><span>
Compare
</span>
</a></li>
</ul>

</li><li data-track-label="issues_menu" class=""><a aria-label="Issues" class="shortcuts-issues has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Issues" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues"><span class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#issues"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="gl-badge badge badge-pill badge-info sm count issue_counter">0
</span></a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Issues
</strong>
<span class="gl-badge badge badge-pill badge-info sm count fly-out-badge issue_counter">0
</span></span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="issue_list" class=""><a aria-label="Issues" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="List" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues"><span>
List
</span>
</a></li><li data-track-label="boards" class=""><a aria-label="Boards" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Boards" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/boards"><span>
Boards
</span>
</a></li><li data-track-label="service_desk" class=""><a aria-label="Service Desk" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Service Desk" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues/service_desk"><span>
Service Desk
</span>
</a></li><li data-track-label="milestones" class=""><a aria-label="Milestones" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Milestones" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>

</li><li data-track-label="merge_requests_menu" class=""><a aria-label="Merge requests" class="shortcuts-merge_requests gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Merge requests" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/merge_requests"><span class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#git-merge"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge requests
</span>
<span class="gl-badge badge badge-pill badge-info sm count merge_counter js-merge-counter">0
</span></a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Merge requests
</strong>
<span class="gl-badge badge badge-pill badge-info sm count fly-out-badge merge_counter js-merge-counter">0
</span></span>
</li></ul>

</li><li data-track-label="ci_cd_menu" class=""><a aria-label="CI/CD" class="shortcuts-pipelines rspec-link-pipelines has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="CI/CD" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/pipelines"><span class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#rocket"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
CI/CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
CI/CD
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="pipelines" class=""><a aria-label="Pipelines" class="shortcuts-pipelines gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Pipelines" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/pipelines"><span>
Pipelines
</span>
</a></li><li data-track-label="pipelines_editor" class=""><a aria-label="Editor" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Editor" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/ci/editor?branch_name=main"><span>
Editor
</span>
</a></li><li data-track-label="jobs" class=""><a aria-label="Jobs" class="shortcuts-builds gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Jobs" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/jobs"><span>
Jobs
</span>
</a></li><li data-track-label="pipeline_schedules" class=""><a aria-label="Schedules" class="shortcuts-builds gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Schedules" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/pipeline_schedules"><span>
Schedules
</span>
</a></li>
</ul>

</li><li data-track-label="security_compliance_menu" class=""><a aria-label="Security &amp; Compliance" class="has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Security &amp; Compliance" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/audit_events"><span class="nav-icon-container">
<svg class="s16" data-testid="shield-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#shield"></use></svg>
</span>
<span class="nav-item-name">
Security &amp; Compliance
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Security &amp; Compliance
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="audit_events" class=""><a aria-label="Audit events" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Audit events" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/audit_events"><span>
Audit events
</span>
</a></li><li data-track-label="configuration" class=""><a aria-label="Configuration" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Configuration" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/security/configuration"><span>
Configuration
</span>
</a></li>
</ul>

</li><li data-track-label="deployments_menu" class=""><a aria-label="Deployments" class="shortcuts-deployments has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Deployments" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/environments"><span class="nav-icon-container">
<svg class="s16" data-testid="deployments-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#deployments"></use></svg>
</span>
<span class="nav-item-name">
Deployments
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Deployments
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="environments" class=""><a aria-label="Environments" class="shortcuts-environments gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Environments" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/environments"><span>
Environments
</span>
</a></li><li data-track-label="feature_flags" class=""><a aria-label="Feature Flags" class="shortcuts-feature-flags gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Feature Flags" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/feature_flags"><span>
Feature Flags
</span>
</a></li><li data-track-label="releases" class=""><a aria-label="Releases" class="shortcuts-deployments-releases gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Releases" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/releases"><span>
Releases
</span>
</a></li>
</ul>

</li><li data-track-label="packages_registries_menu" class=""><a aria-label="Packages and registries" class="has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Packages and registries" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/packages"><span class="nav-icon-container">
<svg class="s16" data-testid="package-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#package"></use></svg>
</span>
<span class="nav-item-name">
Packages and registries
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Packages and registries
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="packages_registry" class=""><a aria-label="Package Registry" class="shortcuts-container-registry gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Package Registry" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/packages"><span>
Package Registry
</span>
</a></li><li data-track-label="container_registry" class=""><a aria-label="Container Registry" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Container Registry" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/container_registry"><span>
Container Registry
</span>
</a></li><li data-track-label="infrastructure_registry" class=""><a aria-label="Infrastructure Registry" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Infrastructure Registry" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/infrastructure_registry"><span>
Infrastructure Registry
</span>
</a></li>
</ul>

</li><li data-track-label="infrastructure_menu" class=""><a aria-label="Infrastructure" class="shortcuts-infrastructure has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Infrastructure" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/clusters"><span class="nav-icon-container">
<svg class="s16" data-testid="cloud-gear-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#cloud-gear"></use></svg>
</span>
<span class="nav-item-name">
Infrastructure
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Infrastructure
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="kubernetes" class=""><a aria-label="Kubernetes clusters" class="shortcuts-kubernetes gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Kubernetes clusters" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/clusters"><span>
Kubernetes clusters
</span>
</a></li><li data-track-label="terraform" class=""><a aria-label="Terraform" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Terraform" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/terraform"><span>
Terraform
</span>
</a></li><li data-track-label="google_cloud" class=""><a aria-label="Google Cloud" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Google Cloud" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/google_cloud/configuration"><span>
Google Cloud
</span>
</a></li>
</ul>

</li><li data-track-label="monitor_menu" class=""><a aria-label="Monitor" class="shortcuts-monitor has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Monitor" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/metrics"><span class="nav-icon-container">
<svg class="s16" data-testid="monitor-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#monitor"></use></svg>
</span>
<span class="nav-item-name">
Monitor
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Monitor
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="metrics" class=""><a aria-label="Metrics" class="shortcuts-metrics gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Metrics" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/metrics"><span>
Metrics
</span>
</a></li><li data-track-label="error_tracking" class=""><a aria-label="Error Tracking" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Error Tracking" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/error_tracking"><span>
Error Tracking
</span>
</a></li><li data-track-label="alert_management" class=""><a aria-label="Alerts" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Alerts" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/alert_management"><span>
Alerts
</span>
</a></li><li data-track-label="incidents" class=""><a aria-label="Incidents" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Incidents" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/incidents"><span>
Incidents
</span>
</a></li>
</ul>

</li><li data-track-label="analytics_menu" class=""><a aria-label="Analytics" class="shortcuts-analytics has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Analytics" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/value_stream_analytics"><span class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chart"></use></svg>
</span>
<span class="nav-item-name">
Analytics
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Analytics
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="cycle_analytics" class=""><a aria-label="Value stream" class="shortcuts-project-cycle-analytics gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Value stream" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/value_stream_analytics"><span>
Value stream
</span>
</a></li><li data-track-label="ci_cd_analytics" class=""><a aria-label="CI/CD" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="CI/CD" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/pipelines/charts"><span>
CI/CD
</span>
</a></li><li data-track-label="repository_analytics" class=""><a aria-label="Repository" class="shortcuts-repository-charts gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Repository" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/graphs/main/charts"><span>
Repository
</span>
</a></li>
</ul>

</li><li data-track-label="wiki_menu" class=""><a aria-label="Wiki" class="shortcuts-wiki gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Wiki" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/wikis/home"><span class="nav-icon-container">
<svg class="s16" data-testid="book-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#book"></use></svg>
</span>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Wiki
</strong>
</span>
</li></ul>

</li><li data-track-label="snippets_menu" class=""><a aria-label="Snippets" class="shortcuts-snippets gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Snippets" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/snippets"><span class="nav-icon-container">
<svg class="s16" data-testid="snippet-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#snippet"></use></svg>
</span>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Snippets
</strong>
</span>
</li></ul>

</li><li data-track-label="settings_menu" class=""><a aria-label="Settings" class="has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Settings" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/edit"><span class="nav-icon-container">
<svg class="s16" data-testid="settings-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#settings"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-settings-link">
Settings
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Settings
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="general" class=""><a aria-label="General" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="General" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/edit"><span>
General
</span>
</a></li><li data-track-label="integrations" class=""><a aria-label="Integrations" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Integrations" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/settings/integrations"><span>
Integrations
</span>
</a></li><li data-track-label="webhooks" class=""><a aria-label="Webhooks" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Webhooks" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/hooks"><span>
Webhooks
</span>
</a></li><li data-track-label="repository" class=""><a aria-label="Repository" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Repository" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/settings/repository"><span>
Repository
</span>
</a></li><li data-track-label="merge_requests" class=""><a aria-label="Merge requests" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Merge requests" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/settings/merge_requests"><span>
Merge requests
</span>
</a></li><li data-track-label="ci_cd" class=""><a aria-label="CI/CD" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="CI/CD" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/settings/ci_cd"><span>
CI/CD
</span>
</a></li><li data-track-label="packages_and_registries" class=""><a aria-label="Packages and registries" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Packages and registries" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/settings/packages_and_registries"><span>
Packages and registries
</span>
</a></li><li data-track-label="pages" class=""><a aria-label="Pages" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Pages" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/pages"><span>
Pages
</span>
</a></li><li data-track-label="monitor" class=""><a aria-label="Monitor" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Monitor" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/settings/operations"><span>
Monitor
</span>
</a></li><li data-track-label="usage_quotas" class=""><a aria-label="Usage Quotas" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Usage Quotas" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/usage_quotas"><span>
Usage Quotas
</span>
</a></li>
</ul>

</li>
<li class="hidden">
<a aria-label="Activity" class="shortcuts-project-activity gl-link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/activity">Activity
</a></li>
<li class="hidden">
<a aria-label="Graph" class="shortcuts-network gl-link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/network/main">Graph
</a></li>
<li class="hidden">
<a aria-label="Create a new issue" class="shortcuts-new-issue gl-link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a aria-label="Jobs" class="shortcuts-builds gl-link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/jobs">Jobs
</a></li>
<li class="hidden">
<a aria-label="Commits" class="shortcuts-commits gl-link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/commits/main">Commits
</a></li>
<li class="hidden">
<a aria-label="Issue Boards" class="shortcuts-issue-boards gl-link" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/boards">Issue Boards
</a></li>

</ul>
<a class="toggle-sidebar-button js-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s12 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-double-lg-left"></use></svg>
<span class="collapse-text gl-ml-3">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg>
<span class="collapse-text gl-ml-3">Close sidebar</span>
</button>
</div>
</aside>


<div class="content-wrapper content-wrapper-margin">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">
























<nav aria-label="Breadcrumbs" class="breadcrumbs container-fluid container-limited project-highlight-puc">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav" data-qa-selector="toggle_mobile_nav_button"><span class="sr-only">Open sidebar</span>
<svg class="s18" data-testid="sidebar-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#sidebar"></use></svg>
</button><div class="breadcrumbs-links" data-qa-selector="breadcrumb_links_content" data-testid="breadcrumb-links">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="https://gitlab.com/mountblue">mountblue</a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"></use></svg></li><li class="expander">
<button aria-label="Show all breadcrumbs" class="text-expander has-tooltip js-breadcrumbs-collapsed-expander" data-container="body" title="Show all breadcrumbs" type="button">
<svg class="s12" data-testid="ellipsis_h-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#ellipsis_h"></use></svg>
</button>
<svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"></use></svg>
</li>
<li class="gl-display-none! breadcrumbs-detail-item">
<a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="https://gitlab.com/mountblue/cohort-22-python">Cohort 22 Python</a>
<svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"></use></svg>
</li>
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="https://gitlab.com/mountblue/cohort-22-python/manish">Manish</a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"></use></svg></li> <li><a href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics"><span class="breadcrumb-item-text js-breadcrumb-item-text">IPL data set analytics</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"></use></svg></li>

<li data-qa-selector="breadcrumb_current_link" data-testid="breadcrumb-current-link">
<a href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md">Repository</a>
</li>
</ul>
</div>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"mountblue","item":"https://gitlab.com/mountblue"},{"@type":"ListItem","position":2,"name":"Cohort 22 Python","item":"https://gitlab.com/mountblue/cohort-22-python"},{"@type":"ListItem","position":3,"name":"Manish","item":"https://gitlab.com/mountblue/cohort-22-python/manish"},{"@type":"ListItem","position":4,"name":"IPL data set analytics","item":"https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics"},{"@type":"ListItem","position":5,"name":"Repository","item":"https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md"}]}

</script>

</div>
</nav>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope="" itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-qa-selector="flash_container">
</div>



<h1 class="page-title gl-font-size-h-display blob-edit-page-title">
Edit file
</h1>
<div class="file-editor">
<ul class="js-edit-mode nav-links gl-border-0 nav gl-tabs-nav"><li class="nav-item active"><a class="nav-link gl-tab-nav-item" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md#editor">Write</a></li>
<li class="nav-item"><a data-preview-url="/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/preview/main/README.md" class="nav-link gl-tab-nav-item" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/edit/main/README.md#preview">Preview</a></li>
</ul><form class="js-quick-submit js-requires-input js-edit-blob-form" data-assets-prefix="/assets" data-blob-filename="README.md" data-project-id="40954144" data-is-markdown="true" data-preview-markdown-path="/mountblue/cohort-22-python/manish/ipl-data-set-analytics/preview_markdown" action="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/update/main/README.md" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" autocomplete="off"><input type="hidden" name="authenticity_token" value="wGbTQphua50gRAKxVixGmSHRPBC7y9DXD8p0Zwrr+AyS4AUP2CoTDvPJlUHtLwaVOoaailstmetpEFeltNctpQ==" autocomplete="off"><div class="file-holder-bottom-radius file-holder file gl-mb-3">
<div class="js-file-title file-title gl-display-flex gl-align-items-center clearfix" data-current-action="edit">
<div class="editor-ref block-truncated has-tooltip" title="main">
<svg class="s12" data-testid="branch-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#branch"></use></svg>
main
</div>
<span class="float-left gl-mr-3"></span>
<input type="text" name="file_path" id="file_path" value="README.md" class="form-control gl-form-input new-file-path js-file-path-name-input">
<div class="template-selectors-menu gl-pl-3" style="display: none;">
<div class="template-selector-dropdowns-wrap">
<div class="template-type-selector js-template-type-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-template-type-selector" type="button" data-qa-selector="template_type_dropdown" data-toggle="dropdown"><span class="dropdown-toggle-text ">Select a template type</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div data-qa-selector="dropdown_list_content" class="dropdown-content "></div><div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div></div></div>
</div>
<div class="license-selector js-license-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-license-selector" type="button" data-data="{&quot;Other&quot;:[{&quot;name&quot;:&quot;GNU Affero General Public License v3.0&quot;,&quot;id&quot;:&quot;agpl-3.0&quot;,&quot;key&quot;:&quot;agpl-3.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;BSD 2-Clause \&quot;Simplified\&quot; License&quot;,&quot;id&quot;:&quot;bsd-2-clause&quot;,&quot;key&quot;:&quot;bsd-2-clause&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;BSD 3-Clause \&quot;New\&quot; or \&quot;Revised\&quot; License&quot;,&quot;id&quot;:&quot;bsd-3-clause&quot;,&quot;key&quot;:&quot;bsd-3-clause&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Boost Software License 1.0&quot;,&quot;id&quot;:&quot;bsl-1.0&quot;,&quot;key&quot;:&quot;bsl-1.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Creative Commons Zero v1.0 Universal&quot;,&quot;id&quot;:&quot;cc0-1.0&quot;,&quot;key&quot;:&quot;cc0-1.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Eclipse Public License 2.0&quot;,&quot;id&quot;:&quot;epl-2.0&quot;,&quot;key&quot;:&quot;epl-2.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;GNU General Public License v2.0&quot;,&quot;id&quot;:&quot;gpl-2.0&quot;,&quot;key&quot;:&quot;gpl-2.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;GNU Lesser General Public License v2.1&quot;,&quot;id&quot;:&quot;lgpl-2.1&quot;,&quot;key&quot;:&quot;lgpl-2.1&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Mozilla Public License 2.0&quot;,&quot;id&quot;:&quot;mpl-2.0&quot;,&quot;key&quot;:&quot;mpl-2.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;The Unlicense&quot;,&quot;id&quot;:&quot;unlicense&quot;,&quot;key&quot;:&quot;unlicense&quot;,&quot;project_id&quot;:40954144}],&quot;Popular&quot;:[{&quot;name&quot;:&quot;Apache License 2.0&quot;,&quot;id&quot;:&quot;apache-2.0&quot;,&quot;key&quot;:&quot;apache-2.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;GNU General Public License v3.0&quot;,&quot;id&quot;:&quot;gpl-3.0&quot;,&quot;key&quot;:&quot;gpl-3.0&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;MIT License&quot;,&quot;id&quot;:&quot;mit&quot;,&quot;key&quot;:&quot;mit&quot;,&quot;project_id&quot;:40954144}]}" data-project="IPL data set analytics" data-fullname="mountblue / Cohort 22 Python / Manish" data-qa-selector="license_dropdown" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Filter" autocomplete="off"><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg></div><div data-qa-selector="dropdown_list_content" class="dropdown-content "></div><div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div></div></div>
</div>
<div class="gitignore-selector js-gitignore-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-gitignore-selector" type="button" data-data="{&quot;Languages&quot;:[{&quot;name&quot;:&quot;Actionscript&quot;,&quot;id&quot;:&quot;Actionscript&quot;,&quot;key&quot;:&quot;Actionscript&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ada&quot;,&quot;id&quot;:&quot;Ada&quot;,&quot;key&quot;:&quot;Ada&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Agda&quot;,&quot;id&quot;:&quot;Agda&quot;,&quot;key&quot;:&quot;Agda&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Android&quot;,&quot;id&quot;:&quot;Android&quot;,&quot;key&quot;:&quot;Android&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;AppEngine&quot;,&quot;id&quot;:&quot;AppEngine&quot;,&quot;key&quot;:&quot;AppEngine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;AppceleratorTitanium&quot;,&quot;id&quot;:&quot;AppceleratorTitanium&quot;,&quot;key&quot;:&quot;AppceleratorTitanium&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ArchLinuxPackages&quot;,&quot;id&quot;:&quot;ArchLinuxPackages&quot;,&quot;key&quot;:&quot;ArchLinuxPackages&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Autotools&quot;,&quot;id&quot;:&quot;Autotools&quot;,&quot;key&quot;:&quot;Autotools&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;C&quot;,&quot;id&quot;:&quot;C&quot;,&quot;key&quot;:&quot;C&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;C++&quot;,&quot;id&quot;:&quot;C++&quot;,&quot;key&quot;:&quot;C++&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CFWheels&quot;,&quot;id&quot;:&quot;CFWheels&quot;,&quot;key&quot;:&quot;CFWheels&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CMake&quot;,&quot;id&quot;:&quot;CMake&quot;,&quot;key&quot;:&quot;CMake&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CUDA&quot;,&quot;id&quot;:&quot;CUDA&quot;,&quot;key&quot;:&quot;CUDA&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CakePHP&quot;,&quot;id&quot;:&quot;CakePHP&quot;,&quot;key&quot;:&quot;CakePHP&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ChefCookbook&quot;,&quot;id&quot;:&quot;ChefCookbook&quot;,&quot;key&quot;:&quot;ChefCookbook&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Clojure&quot;,&quot;id&quot;:&quot;Clojure&quot;,&quot;key&quot;:&quot;Clojure&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CodeIgniter&quot;,&quot;id&quot;:&quot;CodeIgniter&quot;,&quot;key&quot;:&quot;CodeIgniter&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CommonLisp&quot;,&quot;id&quot;:&quot;CommonLisp&quot;,&quot;key&quot;:&quot;CommonLisp&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Composer&quot;,&quot;id&quot;:&quot;Composer&quot;,&quot;key&quot;:&quot;Composer&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Concrete5&quot;,&quot;id&quot;:&quot;Concrete5&quot;,&quot;key&quot;:&quot;Concrete5&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Coq&quot;,&quot;id&quot;:&quot;Coq&quot;,&quot;key&quot;:&quot;Coq&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CraftCMS&quot;,&quot;id&quot;:&quot;CraftCMS&quot;,&quot;key&quot;:&quot;CraftCMS&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;D&quot;,&quot;id&quot;:&quot;D&quot;,&quot;key&quot;:&quot;D&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DM&quot;,&quot;id&quot;:&quot;DM&quot;,&quot;key&quot;:&quot;DM&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Dart&quot;,&quot;id&quot;:&quot;Dart&quot;,&quot;key&quot;:&quot;Dart&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Delphi&quot;,&quot;id&quot;:&quot;Delphi&quot;,&quot;key&quot;:&quot;Delphi&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Drupal&quot;,&quot;id&quot;:&quot;Drupal&quot;,&quot;key&quot;:&quot;Drupal&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;EPiServer&quot;,&quot;id&quot;:&quot;EPiServer&quot;,&quot;key&quot;:&quot;EPiServer&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Eagle&quot;,&quot;id&quot;:&quot;Eagle&quot;,&quot;key&quot;:&quot;Eagle&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Elisp&quot;,&quot;id&quot;:&quot;Elisp&quot;,&quot;key&quot;:&quot;Elisp&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Elixir&quot;,&quot;id&quot;:&quot;Elixir&quot;,&quot;key&quot;:&quot;Elixir&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Elm&quot;,&quot;id&quot;:&quot;Elm&quot;,&quot;key&quot;:&quot;Elm&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Erlang&quot;,&quot;id&quot;:&quot;Erlang&quot;,&quot;key&quot;:&quot;Erlang&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ExpressionEngine&quot;,&quot;id&quot;:&quot;ExpressionEngine&quot;,&quot;key&quot;:&quot;ExpressionEngine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ExtJs&quot;,&quot;id&quot;:&quot;ExtJs&quot;,&quot;key&quot;:&quot;ExtJs&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Fancy&quot;,&quot;id&quot;:&quot;Fancy&quot;,&quot;key&quot;:&quot;Fancy&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Finale&quot;,&quot;id&quot;:&quot;Finale&quot;,&quot;key&quot;:&quot;Finale&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ForceDotCom&quot;,&quot;id&quot;:&quot;ForceDotCom&quot;,&quot;key&quot;:&quot;ForceDotCom&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Fortran&quot;,&quot;id&quot;:&quot;Fortran&quot;,&quot;key&quot;:&quot;Fortran&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;FuelPHP&quot;,&quot;id&quot;:&quot;FuelPHP&quot;,&quot;key&quot;:&quot;FuelPHP&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;GWT&quot;,&quot;id&quot;:&quot;GWT&quot;,&quot;key&quot;:&quot;GWT&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Gcov&quot;,&quot;id&quot;:&quot;Gcov&quot;,&quot;key&quot;:&quot;Gcov&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;GitBook&quot;,&quot;id&quot;:&quot;GitBook&quot;,&quot;key&quot;:&quot;GitBook&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Go&quot;,&quot;id&quot;:&quot;Go&quot;,&quot;key&quot;:&quot;Go&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Godot&quot;,&quot;id&quot;:&quot;Godot&quot;,&quot;key&quot;:&quot;Godot&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Gradle&quot;,&quot;id&quot;:&quot;Gradle&quot;,&quot;key&quot;:&quot;Gradle&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Grails&quot;,&quot;id&quot;:&quot;Grails&quot;,&quot;key&quot;:&quot;Grails&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Haskell&quot;,&quot;id&quot;:&quot;Haskell&quot;,&quot;key&quot;:&quot;Haskell&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;IGORPro&quot;,&quot;id&quot;:&quot;IGORPro&quot;,&quot;key&quot;:&quot;IGORPro&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Idris&quot;,&quot;id&quot;:&quot;Idris&quot;,&quot;key&quot;:&quot;Idris&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Java&quot;,&quot;id&quot;:&quot;Java&quot;,&quot;key&quot;:&quot;Java&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Jboss&quot;,&quot;id&quot;:&quot;Jboss&quot;,&quot;key&quot;:&quot;Jboss&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Jekyll&quot;,&quot;id&quot;:&quot;Jekyll&quot;,&quot;key&quot;:&quot;Jekyll&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Joomla&quot;,&quot;id&quot;:&quot;Joomla&quot;,&quot;key&quot;:&quot;Joomla&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Julia&quot;,&quot;id&quot;:&quot;Julia&quot;,&quot;key&quot;:&quot;Julia&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;KiCad&quot;,&quot;id&quot;:&quot;KiCad&quot;,&quot;key&quot;:&quot;KiCad&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Kohana&quot;,&quot;id&quot;:&quot;Kohana&quot;,&quot;key&quot;:&quot;Kohana&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Kotlin&quot;,&quot;id&quot;:&quot;Kotlin&quot;,&quot;key&quot;:&quot;Kotlin&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;LabVIEW&quot;,&quot;id&quot;:&quot;LabVIEW&quot;,&quot;key&quot;:&quot;LabVIEW&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Laravel&quot;,&quot;id&quot;:&quot;Laravel&quot;,&quot;key&quot;:&quot;Laravel&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Leiningen&quot;,&quot;id&quot;:&quot;Leiningen&quot;,&quot;key&quot;:&quot;Leiningen&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;LemonStand&quot;,&quot;id&quot;:&quot;LemonStand&quot;,&quot;key&quot;:&quot;LemonStand&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Lilypond&quot;,&quot;id&quot;:&quot;Lilypond&quot;,&quot;key&quot;:&quot;Lilypond&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Lithium&quot;,&quot;id&quot;:&quot;Lithium&quot;,&quot;key&quot;:&quot;Lithium&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Lua&quot;,&quot;id&quot;:&quot;Lua&quot;,&quot;key&quot;:&quot;Lua&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Magento&quot;,&quot;id&quot;:&quot;Magento&quot;,&quot;key&quot;:&quot;Magento&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Maven&quot;,&quot;id&quot;:&quot;Maven&quot;,&quot;key&quot;:&quot;Maven&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Mercury&quot;,&quot;id&quot;:&quot;Mercury&quot;,&quot;key&quot;:&quot;Mercury&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;MetaProgrammingSystem&quot;,&quot;id&quot;:&quot;MetaProgrammingSystem&quot;,&quot;key&quot;:&quot;MetaProgrammingSystem&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Nanoc&quot;,&quot;id&quot;:&quot;Nanoc&quot;,&quot;key&quot;:&quot;Nanoc&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Nim&quot;,&quot;id&quot;:&quot;Nim&quot;,&quot;key&quot;:&quot;Nim&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Node&quot;,&quot;id&quot;:&quot;Node&quot;,&quot;key&quot;:&quot;Node&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;OCaml&quot;,&quot;id&quot;:&quot;OCaml&quot;,&quot;key&quot;:&quot;OCaml&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Objective-C&quot;,&quot;id&quot;:&quot;Objective-C&quot;,&quot;key&quot;:&quot;Objective-C&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Opa&quot;,&quot;id&quot;:&quot;Opa&quot;,&quot;key&quot;:&quot;Opa&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;OpenCart&quot;,&quot;id&quot;:&quot;OpenCart&quot;,&quot;key&quot;:&quot;OpenCart&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;OracleForms&quot;,&quot;id&quot;:&quot;OracleForms&quot;,&quot;key&quot;:&quot;OracleForms&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Packer&quot;,&quot;id&quot;:&quot;Packer&quot;,&quot;key&quot;:&quot;Packer&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Perl&quot;,&quot;id&quot;:&quot;Perl&quot;,&quot;key&quot;:&quot;Perl&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Perl6&quot;,&quot;id&quot;:&quot;Perl6&quot;,&quot;key&quot;:&quot;Perl6&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Phalcon&quot;,&quot;id&quot;:&quot;Phalcon&quot;,&quot;key&quot;:&quot;Phalcon&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;PlayFramework&quot;,&quot;id&quot;:&quot;PlayFramework&quot;,&quot;key&quot;:&quot;PlayFramework&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Plone&quot;,&quot;id&quot;:&quot;Plone&quot;,&quot;key&quot;:&quot;Plone&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Prestashop&quot;,&quot;id&quot;:&quot;Prestashop&quot;,&quot;key&quot;:&quot;Prestashop&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Processing&quot;,&quot;id&quot;:&quot;Processing&quot;,&quot;key&quot;:&quot;Processing&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;PureScript&quot;,&quot;id&quot;:&quot;PureScript&quot;,&quot;key&quot;:&quot;PureScript&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Python&quot;,&quot;id&quot;:&quot;Python&quot;,&quot;key&quot;:&quot;Python&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Qooxdoo&quot;,&quot;id&quot;:&quot;Qooxdoo&quot;,&quot;key&quot;:&quot;Qooxdoo&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Qt&quot;,&quot;id&quot;:&quot;Qt&quot;,&quot;key&quot;:&quot;Qt&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;R&quot;,&quot;id&quot;:&quot;R&quot;,&quot;key&quot;:&quot;R&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ROS&quot;,&quot;id&quot;:&quot;ROS&quot;,&quot;key&quot;:&quot;ROS&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Rails&quot;,&quot;id&quot;:&quot;Rails&quot;,&quot;key&quot;:&quot;Rails&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;RhodesRhomobile&quot;,&quot;id&quot;:&quot;RhodesRhomobile&quot;,&quot;key&quot;:&quot;RhodesRhomobile&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ruby&quot;,&quot;id&quot;:&quot;Ruby&quot;,&quot;key&quot;:&quot;Ruby&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Rust&quot;,&quot;id&quot;:&quot;Rust&quot;,&quot;key&quot;:&quot;Rust&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SCons&quot;,&quot;id&quot;:&quot;SCons&quot;,&quot;key&quot;:&quot;SCons&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Sass&quot;,&quot;id&quot;:&quot;Sass&quot;,&quot;key&quot;:&quot;Sass&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Scala&quot;,&quot;id&quot;:&quot;Scala&quot;,&quot;key&quot;:&quot;Scala&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Scheme&quot;,&quot;id&quot;:&quot;Scheme&quot;,&quot;key&quot;:&quot;Scheme&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Scrivener&quot;,&quot;id&quot;:&quot;Scrivener&quot;,&quot;key&quot;:&quot;Scrivener&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Sdcc&quot;,&quot;id&quot;:&quot;Sdcc&quot;,&quot;key&quot;:&quot;Sdcc&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SeamGen&quot;,&quot;id&quot;:&quot;SeamGen&quot;,&quot;key&quot;:&quot;SeamGen&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SketchUp&quot;,&quot;id&quot;:&quot;SketchUp&quot;,&quot;key&quot;:&quot;SketchUp&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Smalltalk&quot;,&quot;id&quot;:&quot;Smalltalk&quot;,&quot;key&quot;:&quot;Smalltalk&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Stella&quot;,&quot;id&quot;:&quot;Stella&quot;,&quot;key&quot;:&quot;Stella&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SugarCRM&quot;,&quot;id&quot;:&quot;SugarCRM&quot;,&quot;key&quot;:&quot;SugarCRM&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Swift&quot;,&quot;id&quot;:&quot;Swift&quot;,&quot;key&quot;:&quot;Swift&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Symfony&quot;,&quot;id&quot;:&quot;Symfony&quot;,&quot;key&quot;:&quot;Symfony&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SymphonyCMS&quot;,&quot;id&quot;:&quot;SymphonyCMS&quot;,&quot;key&quot;:&quot;SymphonyCMS&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;TeX&quot;,&quot;id&quot;:&quot;TeX&quot;,&quot;key&quot;:&quot;TeX&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Terraform&quot;,&quot;id&quot;:&quot;Terraform&quot;,&quot;key&quot;:&quot;Terraform&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Textpattern&quot;,&quot;id&quot;:&quot;Textpattern&quot;,&quot;key&quot;:&quot;Textpattern&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;TurboGears2&quot;,&quot;id&quot;:&quot;TurboGears2&quot;,&quot;key&quot;:&quot;TurboGears2&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Typo3&quot;,&quot;id&quot;:&quot;Typo3&quot;,&quot;key&quot;:&quot;Typo3&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Umbraco&quot;,&quot;id&quot;:&quot;Umbraco&quot;,&quot;key&quot;:&quot;Umbraco&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Unity&quot;,&quot;id&quot;:&quot;Unity&quot;,&quot;key&quot;:&quot;Unity&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;UnrealEngine&quot;,&quot;id&quot;:&quot;UnrealEngine&quot;,&quot;key&quot;:&quot;UnrealEngine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;VVVV&quot;,&quot;id&quot;:&quot;VVVV&quot;,&quot;key&quot;:&quot;VVVV&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;VisualStudio&quot;,&quot;id&quot;:&quot;VisualStudio&quot;,&quot;key&quot;:&quot;VisualStudio&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Waf&quot;,&quot;id&quot;:&quot;Waf&quot;,&quot;key&quot;:&quot;Waf&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;WordPress&quot;,&quot;id&quot;:&quot;WordPress&quot;,&quot;key&quot;:&quot;WordPress&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Xojo&quot;,&quot;id&quot;:&quot;Xojo&quot;,&quot;key&quot;:&quot;Xojo&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Yeoman&quot;,&quot;id&quot;:&quot;Yeoman&quot;,&quot;key&quot;:&quot;Yeoman&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Yii&quot;,&quot;id&quot;:&quot;Yii&quot;,&quot;key&quot;:&quot;Yii&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ZendFramework&quot;,&quot;id&quot;:&quot;ZendFramework&quot;,&quot;key&quot;:&quot;ZendFramework&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Zephir&quot;,&quot;id&quot;:&quot;Zephir&quot;,&quot;key&quot;:&quot;Zephir&quot;,&quot;project_id&quot;:40954144}],&quot;Global&quot;:[{&quot;name&quot;:&quot;Anjuta&quot;,&quot;id&quot;:&quot;Anjuta&quot;,&quot;key&quot;:&quot;Anjuta&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ansible&quot;,&quot;id&quot;:&quot;Ansible&quot;,&quot;key&quot;:&quot;Ansible&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Archives&quot;,&quot;id&quot;:&quot;Archives&quot;,&quot;key&quot;:&quot;Archives&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Backup&quot;,&quot;id&quot;:&quot;Backup&quot;,&quot;key&quot;:&quot;Backup&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Bazaar&quot;,&quot;id&quot;:&quot;Bazaar&quot;,&quot;key&quot;:&quot;Bazaar&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;BricxCC&quot;,&quot;id&quot;:&quot;BricxCC&quot;,&quot;key&quot;:&quot;BricxCC&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CVS&quot;,&quot;id&quot;:&quot;CVS&quot;,&quot;key&quot;:&quot;CVS&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Calabash&quot;,&quot;id&quot;:&quot;Calabash&quot;,&quot;key&quot;:&quot;Calabash&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Cloud9&quot;,&quot;id&quot;:&quot;Cloud9&quot;,&quot;key&quot;:&quot;Cloud9&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;CodeKit&quot;,&quot;id&quot;:&quot;CodeKit&quot;,&quot;key&quot;:&quot;CodeKit&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DartEditor&quot;,&quot;id&quot;:&quot;DartEditor&quot;,&quot;key&quot;:&quot;DartEditor&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Diff&quot;,&quot;id&quot;:&quot;Diff&quot;,&quot;key&quot;:&quot;Diff&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Dreamweaver&quot;,&quot;id&quot;:&quot;Dreamweaver&quot;,&quot;key&quot;:&quot;Dreamweaver&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Dropbox&quot;,&quot;id&quot;:&quot;Dropbox&quot;,&quot;key&quot;:&quot;Dropbox&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Eclipse&quot;,&quot;id&quot;:&quot;Eclipse&quot;,&quot;key&quot;:&quot;Eclipse&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;EiffelStudio&quot;,&quot;id&quot;:&quot;EiffelStudio&quot;,&quot;key&quot;:&quot;EiffelStudio&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Emacs&quot;,&quot;id&quot;:&quot;Emacs&quot;,&quot;key&quot;:&quot;Emacs&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ensime&quot;,&quot;id&quot;:&quot;Ensime&quot;,&quot;key&quot;:&quot;Ensime&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Espresso&quot;,&quot;id&quot;:&quot;Espresso&quot;,&quot;key&quot;:&quot;Espresso&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;FlexBuilder&quot;,&quot;id&quot;:&quot;FlexBuilder&quot;,&quot;key&quot;:&quot;FlexBuilder&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;GPG&quot;,&quot;id&quot;:&quot;GPG&quot;,&quot;key&quot;:&quot;GPG&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Images&quot;,&quot;id&quot;:&quot;Images&quot;,&quot;key&quot;:&quot;Images&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;JDeveloper&quot;,&quot;id&quot;:&quot;JDeveloper&quot;,&quot;key&quot;:&quot;JDeveloper&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;JEnv&quot;,&quot;id&quot;:&quot;JEnv&quot;,&quot;key&quot;:&quot;JEnv&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;JetBrains&quot;,&quot;id&quot;:&quot;JetBrains&quot;,&quot;key&quot;:&quot;JetBrains&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;KDevelop4&quot;,&quot;id&quot;:&quot;KDevelop4&quot;,&quot;key&quot;:&quot;KDevelop4&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Kate&quot;,&quot;id&quot;:&quot;Kate&quot;,&quot;key&quot;:&quot;Kate&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Lazarus&quot;,&quot;id&quot;:&quot;Lazarus&quot;,&quot;key&quot;:&quot;Lazarus&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;LibreOffice&quot;,&quot;id&quot;:&quot;LibreOffice&quot;,&quot;key&quot;:&quot;LibreOffice&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Linux&quot;,&quot;id&quot;:&quot;Linux&quot;,&quot;key&quot;:&quot;Linux&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;LyX&quot;,&quot;id&quot;:&quot;LyX&quot;,&quot;key&quot;:&quot;LyX&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Matlab&quot;,&quot;id&quot;:&quot;Matlab&quot;,&quot;key&quot;:&quot;Matlab&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Mercurial&quot;,&quot;id&quot;:&quot;Mercurial&quot;,&quot;key&quot;:&quot;Mercurial&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;MicrosoftOffice&quot;,&quot;id&quot;:&quot;MicrosoftOffice&quot;,&quot;key&quot;:&quot;MicrosoftOffice&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ModelSim&quot;,&quot;id&quot;:&quot;ModelSim&quot;,&quot;key&quot;:&quot;ModelSim&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Momentics&quot;,&quot;id&quot;:&quot;Momentics&quot;,&quot;key&quot;:&quot;Momentics&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;MonoDevelop&quot;,&quot;id&quot;:&quot;MonoDevelop&quot;,&quot;key&quot;:&quot;MonoDevelop&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;NetBeans&quot;,&quot;id&quot;:&quot;NetBeans&quot;,&quot;key&quot;:&quot;NetBeans&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ninja&quot;,&quot;id&quot;:&quot;Ninja&quot;,&quot;key&quot;:&quot;Ninja&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;NotepadPP&quot;,&quot;id&quot;:&quot;NotepadPP&quot;,&quot;key&quot;:&quot;NotepadPP&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Otto&quot;,&quot;id&quot;:&quot;Otto&quot;,&quot;key&quot;:&quot;Otto&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;PSoCCreator&quot;,&quot;id&quot;:&quot;PSoCCreator&quot;,&quot;key&quot;:&quot;PSoCCreator&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Patch&quot;,&quot;id&quot;:&quot;Patch&quot;,&quot;key&quot;:&quot;Patch&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;PuTTY&quot;,&quot;id&quot;:&quot;PuTTY&quot;,&quot;key&quot;:&quot;PuTTY&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Redcar&quot;,&quot;id&quot;:&quot;Redcar&quot;,&quot;key&quot;:&quot;Redcar&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Redis&quot;,&quot;id&quot;:&quot;Redis&quot;,&quot;key&quot;:&quot;Redis&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SBT&quot;,&quot;id&quot;:&quot;SBT&quot;,&quot;key&quot;:&quot;SBT&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SVN&quot;,&quot;id&quot;:&quot;SVN&quot;,&quot;key&quot;:&quot;SVN&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SlickEdit&quot;,&quot;id&quot;:&quot;SlickEdit&quot;,&quot;key&quot;:&quot;SlickEdit&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Stata&quot;,&quot;id&quot;:&quot;Stata&quot;,&quot;key&quot;:&quot;Stata&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SublimeText&quot;,&quot;id&quot;:&quot;SublimeText&quot;,&quot;key&quot;:&quot;SublimeText&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SynopsysVCS&quot;,&quot;id&quot;:&quot;SynopsysVCS&quot;,&quot;key&quot;:&quot;SynopsysVCS&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Tags&quot;,&quot;id&quot;:&quot;Tags&quot;,&quot;key&quot;:&quot;Tags&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;TextMate&quot;,&quot;id&quot;:&quot;TextMate&quot;,&quot;key&quot;:&quot;TextMate&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;TortoiseGit&quot;,&quot;id&quot;:&quot;TortoiseGit&quot;,&quot;key&quot;:&quot;TortoiseGit&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Vagrant&quot;,&quot;id&quot;:&quot;Vagrant&quot;,&quot;key&quot;:&quot;Vagrant&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Vim&quot;,&quot;id&quot;:&quot;Vim&quot;,&quot;key&quot;:&quot;Vim&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;VirtualEnv&quot;,&quot;id&quot;:&quot;VirtualEnv&quot;,&quot;key&quot;:&quot;VirtualEnv&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Virtuoso&quot;,&quot;id&quot;:&quot;Virtuoso&quot;,&quot;key&quot;:&quot;Virtuoso&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;VisualStudioCode&quot;,&quot;id&quot;:&quot;VisualStudioCode&quot;,&quot;key&quot;:&quot;VisualStudioCode&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;WebMethods&quot;,&quot;id&quot;:&quot;WebMethods&quot;,&quot;key&quot;:&quot;WebMethods&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Windows&quot;,&quot;id&quot;:&quot;Windows&quot;,&quot;key&quot;:&quot;Windows&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Xcode&quot;,&quot;id&quot;:&quot;Xcode&quot;,&quot;key&quot;:&quot;Xcode&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;XilinxISE&quot;,&quot;id&quot;:&quot;XilinxISE&quot;,&quot;key&quot;:&quot;XilinxISE&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;macOS&quot;,&quot;id&quot;:&quot;macOS&quot;,&quot;key&quot;:&quot;macOS&quot;,&quot;project_id&quot;:40954144}]}" data-qa-selector="gitignore_dropdown" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Filter" autocomplete="off"><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg></div><div data-qa-selector="dropdown_list_content" class="dropdown-content "></div><div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div></div></div>
</div>
<div class="metrics-dashboard-selector js-metrics-dashboard-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-metrics-dashboard-selector" type="button" data-data="{&quot;General&quot;:[{&quot;name&quot;:&quot;Area&quot;,&quot;id&quot;:&quot;Area&quot;,&quot;key&quot;:&quot;Area&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Default&quot;,&quot;id&quot;:&quot;Default&quot;,&quot;key&quot;:&quot;Default&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;gauge&quot;,&quot;id&quot;:&quot;gauge&quot;,&quot;key&quot;:&quot;gauge&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;k8s_area&quot;,&quot;id&quot;:&quot;k8s_area&quot;,&quot;key&quot;:&quot;k8s_area&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;k8s_gauge&quot;,&quot;id&quot;:&quot;k8s_gauge&quot;,&quot;key&quot;:&quot;k8s_gauge&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;k8s_single-stat&quot;,&quot;id&quot;:&quot;k8s_single-stat&quot;,&quot;key&quot;:&quot;k8s_single-stat&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;single-stat&quot;,&quot;id&quot;:&quot;single-stat&quot;,&quot;key&quot;:&quot;single-stat&quot;,&quot;project_id&quot;:40954144}]}" data-qa-selector="metrics_dashboard_dropdown" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Filter" autocomplete="off"><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg></div><div data-qa-selector="dropdown_list_content" class="dropdown-content "></div><div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div></div></div>
</div>
<div class="gitlab-ci-yml-selector js-gitlab-ci-yml-selector-wrap js-template-selector-wrap hidden" id="gitlab-ci-yml-selector">
<div class="dropdown "><button class="dropdown-menu-toggle js-gitlab-ci-yml-selector" type="button" data-data="{&quot;General&quot;:[{&quot;name&quot;:&quot;5-Minute-Production-App&quot;,&quot;id&quot;:&quot;5-Minute-Production-App&quot;,&quot;key&quot;:&quot;5-Minute-Production-App&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Android&quot;,&quot;id&quot;:&quot;Android&quot;,&quot;key&quot;:&quot;Android&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Android-Fastlane&quot;,&quot;id&quot;:&quot;Android-Fastlane&quot;,&quot;key&quot;:&quot;Android-Fastlane&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Auto-DevOps&quot;,&quot;id&quot;:&quot;Auto-DevOps&quot;,&quot;key&quot;:&quot;Auto-DevOps&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Bash&quot;,&quot;id&quot;:&quot;Bash&quot;,&quot;key&quot;:&quot;Bash&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;C++&quot;,&quot;id&quot;:&quot;C++&quot;,&quot;key&quot;:&quot;C++&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Chef&quot;,&quot;id&quot;:&quot;Chef&quot;,&quot;key&quot;:&quot;Chef&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Clojure&quot;,&quot;id&quot;:&quot;Clojure&quot;,&quot;key&quot;:&quot;Clojure&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Code-Quality&quot;,&quot;id&quot;:&quot;Code-Quality&quot;,&quot;key&quot;:&quot;Code-Quality&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Composer&quot;,&quot;id&quot;:&quot;Composer&quot;,&quot;key&quot;:&quot;Composer&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Crystal&quot;,&quot;id&quot;:&quot;Crystal&quot;,&quot;key&quot;:&quot;Crystal&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Dart&quot;,&quot;id&quot;:&quot;Dart&quot;,&quot;key&quot;:&quot;Dart&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Deploy-ECS&quot;,&quot;id&quot;:&quot;Deploy-ECS&quot;,&quot;key&quot;:&quot;Deploy-ECS&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Django&quot;,&quot;id&quot;:&quot;Django&quot;,&quot;key&quot;:&quot;Django&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Docker&quot;,&quot;id&quot;:&quot;Docker&quot;,&quot;key&quot;:&quot;Docker&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Elixir&quot;,&quot;id&quot;:&quot;Elixir&quot;,&quot;key&quot;:&quot;Elixir&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Flutter&quot;,&quot;id&quot;:&quot;Flutter&quot;,&quot;key&quot;:&quot;Flutter&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Getting-Started&quot;,&quot;id&quot;:&quot;Getting-Started&quot;,&quot;key&quot;:&quot;Getting-Started&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Go&quot;,&quot;id&quot;:&quot;Go&quot;,&quot;key&quot;:&quot;Go&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Gradle&quot;,&quot;id&quot;:&quot;Gradle&quot;,&quot;key&quot;:&quot;Gradle&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Grails&quot;,&quot;id&quot;:&quot;Grails&quot;,&quot;key&quot;:&quot;Grails&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Indeni.Cloudrail&quot;,&quot;id&quot;:&quot;Indeni.Cloudrail&quot;,&quot;key&quot;:&quot;Indeni.Cloudrail&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Julia&quot;,&quot;id&quot;:&quot;Julia&quot;,&quot;key&quot;:&quot;Julia&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Kaniko&quot;,&quot;id&quot;:&quot;Kaniko&quot;,&quot;key&quot;:&quot;Kaniko&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Katalon&quot;,&quot;id&quot;:&quot;Katalon&quot;,&quot;key&quot;:&quot;Katalon&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;LaTeX&quot;,&quot;id&quot;:&quot;LaTeX&quot;,&quot;key&quot;:&quot;LaTeX&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Laravel&quot;,&quot;id&quot;:&quot;Laravel&quot;,&quot;key&quot;:&quot;Laravel&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;MATLAB&quot;,&quot;id&quot;:&quot;MATLAB&quot;,&quot;key&quot;:&quot;MATLAB&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Maven&quot;,&quot;id&quot;:&quot;Maven&quot;,&quot;key&quot;:&quot;Maven&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Mono&quot;,&quot;id&quot;:&quot;Mono&quot;,&quot;key&quot;:&quot;Mono&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Nodejs&quot;,&quot;id&quot;:&quot;Nodejs&quot;,&quot;key&quot;:&quot;Nodejs&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;OpenShift&quot;,&quot;id&quot;:&quot;OpenShift&quot;,&quot;key&quot;:&quot;OpenShift&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;PHP&quot;,&quot;id&quot;:&quot;PHP&quot;,&quot;key&quot;:&quot;PHP&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Packer&quot;,&quot;id&quot;:&quot;Packer&quot;,&quot;key&quot;:&quot;Packer&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Python&quot;,&quot;id&quot;:&quot;Python&quot;,&quot;key&quot;:&quot;Python&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Qualys-IaC-Security&quot;,&quot;id&quot;:&quot;Qualys-IaC-Security&quot;,&quot;key&quot;:&quot;Qualys-IaC-Security&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ruby&quot;,&quot;id&quot;:&quot;Ruby&quot;,&quot;key&quot;:&quot;Ruby&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Rust&quot;,&quot;id&quot;:&quot;Rust&quot;,&quot;key&quot;:&quot;Rust&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Scala&quot;,&quot;id&quot;:&quot;Scala&quot;,&quot;key&quot;:&quot;Scala&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Swift&quot;,&quot;id&quot;:&quot;Swift&quot;,&quot;key&quot;:&quot;Swift&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Terraform&quot;,&quot;id&quot;:&quot;Terraform&quot;,&quot;key&quot;:&quot;Terraform&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;ThemeKit&quot;,&quot;id&quot;:&quot;ThemeKit&quot;,&quot;key&quot;:&quot;ThemeKit&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;dotNET&quot;,&quot;id&quot;:&quot;dotNET&quot;,&quot;key&quot;:&quot;dotNET&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;dotNET-Core&quot;,&quot;id&quot;:&quot;dotNET-Core&quot;,&quot;key&quot;:&quot;dotNET-Core&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;iOS-Fastlane&quot;,&quot;id&quot;:&quot;iOS-Fastlane&quot;,&quot;key&quot;:&quot;iOS-Fastlane&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;liquibase&quot;,&quot;id&quot;:&quot;liquibase&quot;,&quot;key&quot;:&quot;liquibase&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;npm&quot;,&quot;id&quot;:&quot;npm&quot;,&quot;key&quot;:&quot;npm&quot;,&quot;project_id&quot;:40954144}],&quot;Pages&quot;:[{&quot;name&quot;:&quot;Brunch&quot;,&quot;id&quot;:&quot;Brunch&quot;,&quot;key&quot;:&quot;Brunch&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Doxygen&quot;,&quot;id&quot;:&quot;Doxygen&quot;,&quot;key&quot;:&quot;Doxygen&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Gatsby&quot;,&quot;id&quot;:&quot;Gatsby&quot;,&quot;key&quot;:&quot;Gatsby&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;HTML&quot;,&quot;id&quot;:&quot;HTML&quot;,&quot;key&quot;:&quot;HTML&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Harp&quot;,&quot;id&quot;:&quot;Harp&quot;,&quot;key&quot;:&quot;Harp&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Hexo&quot;,&quot;id&quot;:&quot;Hexo&quot;,&quot;key&quot;:&quot;Hexo&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Hugo&quot;,&quot;id&quot;:&quot;Hugo&quot;,&quot;key&quot;:&quot;Hugo&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Hyde&quot;,&quot;id&quot;:&quot;Hyde&quot;,&quot;key&quot;:&quot;Hyde&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;JBake&quot;,&quot;id&quot;:&quot;JBake&quot;,&quot;key&quot;:&quot;JBake&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Jekyll&quot;,&quot;id&quot;:&quot;Jekyll&quot;,&quot;key&quot;:&quot;Jekyll&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Jigsaw&quot;,&quot;id&quot;:&quot;Jigsaw&quot;,&quot;key&quot;:&quot;Jigsaw&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Lektor&quot;,&quot;id&quot;:&quot;Lektor&quot;,&quot;key&quot;:&quot;Lektor&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Metalsmith&quot;,&quot;id&quot;:&quot;Metalsmith&quot;,&quot;key&quot;:&quot;Metalsmith&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Middleman&quot;,&quot;id&quot;:&quot;Middleman&quot;,&quot;key&quot;:&quot;Middleman&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Nanoc&quot;,&quot;id&quot;:&quot;Nanoc&quot;,&quot;key&quot;:&quot;Nanoc&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Octopress&quot;,&quot;id&quot;:&quot;Octopress&quot;,&quot;key&quot;:&quot;Octopress&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Pelican&quot;,&quot;id&quot;:&quot;Pelican&quot;,&quot;key&quot;:&quot;Pelican&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SwaggerUI&quot;,&quot;id&quot;:&quot;SwaggerUI&quot;,&quot;key&quot;:&quot;SwaggerUI&quot;,&quot;project_id&quot;:40954144}],&quot;Verify&quot;:[{&quot;name&quot;:&quot;Accessibility&quot;,&quot;id&quot;:&quot;Accessibility&quot;,&quot;key&quot;:&quot;Accessibility&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Browser-Performance&quot;,&quot;id&quot;:&quot;Browser-Performance&quot;,&quot;key&quot;:&quot;Browser-Performance&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;FailFast&quot;,&quot;id&quot;:&quot;FailFast&quot;,&quot;key&quot;:&quot;FailFast&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Load-Performance-Testing&quot;,&quot;id&quot;:&quot;Load-Performance-Testing&quot;,&quot;key&quot;:&quot;Load-Performance-Testing&quot;,&quot;project_id&quot;:40954144}],&quot;Security&quot;:[{&quot;name&quot;:&quot;API-Fuzzing&quot;,&quot;id&quot;:&quot;API-Fuzzing&quot;,&quot;key&quot;:&quot;API-Fuzzing&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Container-Scanning&quot;,&quot;id&quot;:&quot;Container-Scanning&quot;,&quot;key&quot;:&quot;Container-Scanning&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Coverage-Fuzzing&quot;,&quot;id&quot;:&quot;Coverage-Fuzzing&quot;,&quot;key&quot;:&quot;Coverage-Fuzzing&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DAST&quot;,&quot;id&quot;:&quot;DAST&quot;,&quot;key&quot;:&quot;DAST&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DAST-API&quot;,&quot;id&quot;:&quot;DAST-API&quot;,&quot;key&quot;:&quot;DAST-API&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DAST-On-Demand-API-Scan&quot;,&quot;id&quot;:&quot;DAST-On-Demand-API-Scan&quot;,&quot;key&quot;:&quot;DAST-On-Demand-API-Scan&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DAST-On-Demand-Scan&quot;,&quot;id&quot;:&quot;DAST-On-Demand-Scan&quot;,&quot;key&quot;:&quot;DAST-On-Demand-Scan&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;DAST-Runner-Validation&quot;,&quot;id&quot;:&quot;DAST-Runner-Validation&quot;,&quot;key&quot;:&quot;DAST-Runner-Validation&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Dependency-Scanning&quot;,&quot;id&quot;:&quot;Dependency-Scanning&quot;,&quot;key&quot;:&quot;Dependency-Scanning&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Fortify-FoD-sast&quot;,&quot;id&quot;:&quot;Fortify-FoD-sast&quot;,&quot;key&quot;:&quot;Fortify-FoD-sast&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;License-Scanning&quot;,&quot;id&quot;:&quot;License-Scanning&quot;,&quot;key&quot;:&quot;License-Scanning&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SAST&quot;,&quot;id&quot;:&quot;SAST&quot;,&quot;key&quot;:&quot;SAST&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;SAST-IaC&quot;,&quot;id&quot;:&quot;SAST-IaC&quot;,&quot;key&quot;:&quot;SAST-IaC&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Secret-Detection&quot;,&quot;id&quot;:&quot;Secret-Detection&quot;,&quot;key&quot;:&quot;Secret-Detection&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Secure-Binaries&quot;,&quot;id&quot;:&quot;Secure-Binaries&quot;,&quot;key&quot;:&quot;Secure-Binaries&quot;,&quot;project_id&quot;:40954144}]}" data-qa-selector="gitlab_ci_yml_dropdown" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Filter" autocomplete="off"><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg></div><div data-qa-selector="dropdown_list_content" class="dropdown-content "></div><div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div></div></div>
</div>
<div class="dockerfile-selector js-dockerfile-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-dockerfile-selector" type="button" data-data="{&quot;General&quot;:[{&quot;name&quot;:&quot;Binary&quot;,&quot;id&quot;:&quot;Binary&quot;,&quot;key&quot;:&quot;Binary&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Binary-alpine&quot;,&quot;id&quot;:&quot;Binary-alpine&quot;,&quot;key&quot;:&quot;Binary-alpine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Binary-scratch&quot;,&quot;id&quot;:&quot;Binary-scratch&quot;,&quot;key&quot;:&quot;Binary-scratch&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Golang&quot;,&quot;id&quot;:&quot;Golang&quot;,&quot;key&quot;:&quot;Golang&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Golang-alpine&quot;,&quot;id&quot;:&quot;Golang-alpine&quot;,&quot;key&quot;:&quot;Golang-alpine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Golang-scratch&quot;,&quot;id&quot;:&quot;Golang-scratch&quot;,&quot;key&quot;:&quot;Golang-scratch&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;HTTPd&quot;,&quot;id&quot;:&quot;HTTPd&quot;,&quot;key&quot;:&quot;HTTPd&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Node&quot;,&quot;id&quot;:&quot;Node&quot;,&quot;key&quot;:&quot;Node&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Node-alpine&quot;,&quot;id&quot;:&quot;Node-alpine&quot;,&quot;key&quot;:&quot;Node-alpine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;OpenJDK&quot;,&quot;id&quot;:&quot;OpenJDK&quot;,&quot;key&quot;:&quot;OpenJDK&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;PHP&quot;,&quot;id&quot;:&quot;PHP&quot;,&quot;key&quot;:&quot;PHP&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Python&quot;,&quot;id&quot;:&quot;Python&quot;,&quot;key&quot;:&quot;Python&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Python-alpine&quot;,&quot;id&quot;:&quot;Python-alpine&quot;,&quot;key&quot;:&quot;Python-alpine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Python2&quot;,&quot;id&quot;:&quot;Python2&quot;,&quot;key&quot;:&quot;Python2&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ruby&quot;,&quot;id&quot;:&quot;Ruby&quot;,&quot;key&quot;:&quot;Ruby&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Ruby-alpine&quot;,&quot;id&quot;:&quot;Ruby-alpine&quot;,&quot;key&quot;:&quot;Ruby-alpine&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Rust&quot;,&quot;id&quot;:&quot;Rust&quot;,&quot;key&quot;:&quot;Rust&quot;,&quot;project_id&quot;:40954144},{&quot;name&quot;:&quot;Swift&quot;,&quot;id&quot;:&quot;Swift&quot;,&quot;key&quot;:&quot;Swift&quot;,&quot;project_id&quot;:40954144}]}" data-qa-selector="dockerfile_dropdown" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Filter" autocomplete="off"><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"></use></svg></div><div data-qa-selector="dropdown_list_content" class="dropdown-content "></div><div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div></div></div>
</div>
</div>
</div>

<div class="file-buttons gl-display-flex gl-align-items-center gl-justify-content-end">
<div class="md-header-toolbar active">
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="**" data-md-shortcuts="[&quot;mod+b&quot;]" data-container="body" title="Add bold text (Ctrl+B)" aria-label="Add bold text (Ctrl+B)"><svg class="s16" data-testid="bold-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#bold"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="_" data-md-shortcuts="[&quot;mod+i&quot;]" data-container="body" title="Add italic text (Ctrl+I)" aria-label="Add italic text (Ctrl+I)"><svg class="s16" data-testid="italic-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#italic"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="~~" data-md-shortcuts="[&quot;mod+shift+x&quot;]" data-container="body" title="Add strikethrough text (Ctrl+⇧X)" aria-label="Add strikethrough text (Ctrl+⇧X)"><svg class="s16" data-testid="strikethrough-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#strikethrough"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="&gt; " data-md-prepend="true" data-container="body" title="Insert a quote" aria-label="Insert a quote"><svg class="s16" data-testid="quote-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#quote"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="`" data-md-block="```" data-container="body" title="Insert code" aria-label="Insert code"><svg class="s16" data-testid="code-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#code"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="[{text}](url)" data-md-select="url" data-md-shortcuts="[&quot;mod+k&quot;]" data-container="body" title="Add a link (Ctrl+K)" aria-label="Add a link (Ctrl+K)"><svg class="s16" data-testid="link-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#link"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="- " data-md-prepend="true" data-container="body" title="Add a bullet list" aria-label="Add a bullet list"><svg class="s16" data-testid="list-bulleted-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#list-bulleted"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="1. " data-md-prepend="true" data-container="body" title="Add a numbered list" aria-label="Add a numbered list"><svg class="s16" data-testid="list-numbered-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#list-numbered"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="- [ ] " data-md-prepend="true" data-container="body" title="Add a checklist" aria-label="Add a checklist"><svg class="s16" data-testid="list-task-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#list-task"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip gl-display-none" data-md-command="indentLines" data-md-shortcuts="[&quot;mod+]&quot;]" data-container="body" title="Indent line (Ctrl+])" aria-label="Indent line (Ctrl+])"><svg class="s16" data-testid="list-indent-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#list-indent"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip gl-display-none" data-md-command="outdentLines" data-md-shortcuts="[&quot;mod+[&quot;]" data-container="body" title="Outdent line (Ctrl+[)" aria-label="Outdent line (Ctrl+[)"><svg class="s16" data-testid="list-outdent-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#list-outdent"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="&lt;details&gt;&lt;summary&gt;Click to expand&lt;/summary&gt;
{text}
&lt;/details&gt;" data-md-prepend="true" data-md-select="Click to expand" data-container="body" title="Add a collapsible section" aria-label="Add a collapsible section"><svg class="s16" data-testid="details-block-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#details-block"></use></svg></button>
<button type="button" class="gl-button btn btn-default-tertiary btn-icon js-md has-tooltip " data-md-tag="| header | header |
| ------ | ------ |
|        |        |
|        |        |" data-md-prepend="true" data-container="body" title="Add a table" aria-label="Add a table"><svg class="s16" data-testid="table-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#table"></use></svg></button>
</div>

<span class="soft-wrap-toggle soft-wrap-active">
<button class="gl-button btn btn-md btn-default no-wrap" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="soft-unwrap-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#soft-unwrap"></use></svg>
<span class="gl-button-text">
No wrap

</span>

</button><button class="gl-button btn btn-md btn-default soft-wrap" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="soft-wrap-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#soft-wrap"></use></svg>
<span class="gl-button-text">
Soft wrap

</span>

</button></span>
</div>
</div>
<div class="file-editor code">
<div class="js-edit-mode-pane" data-qa-selector="source_editor_preview_container" id="editor" data-keybinding-context="1" style="--codelens-font-features_ee1f61:&quot;liga&quot; off, &quot;calt&quot; off;" data-mode-id="markdown"><div class="monaco-editor gl-source-editor no-user-select  showUnused showDeprecated vs focused" role="code" data-uri="file:///gitlab/2f7b0b46-1d48-412c-b205-789fb8f07ba2/README.md" style="width: 987px; height: 500px;"><div data-mprt="3" class="overflow-guard" style="width: 987px; height: 500px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; height: 500px; width: 87px;"><div class="glyph-margin" style="left: 0px; width: 19px; height: 500px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays focused" role="presentation" aria-hidden="true" style="position: absolute; width: 87px; font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; height: 500px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">3</div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">4</div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">5</div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">6</div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:87px; height:19px;"></div><div class="active-line-number line-numbers lh-odd" style="left:19px;width:42px;">7</div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">8</div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">9</div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">10</div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">11</div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">12</div></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">13</div></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">14</div></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:19px;width:42px;">15</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 87px; width: 900px; height: 500px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; left: 0px;"><div class="view-overlays focused" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 900px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="current-line" style="width:900px; height:19px;"></div><div class="cdr selectionHighlight" style="left:25px;width:101px;height:19px;"></div></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; width: 900px; height: 500px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk10 mtkb">##&nbsp;Name</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">IPL&nbsp;dataset&nbsp;Analysis</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk10 mtkb">##&nbsp;Description</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">This&nbsp;projects&nbsp;does&nbsp;different&nbsp;different&nbsp;comperisons</span><span class="mtk1">&nbsp;with&nbsp;the&nbsp;given&nbsp;dataset&nbsp;and&nbsp;visualisez&nbsp;them.&nbsp;</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk10 mtkb">##&nbsp;Installation</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">Check&nbsp;out&nbsp;the&nbsp;requirements.txt&nbsp;file&nbsp;and&nbsp;install&nbsp;th</span><span class="mtk1">em&nbsp;in&nbsp;your&nbsp;local&nbsp;system.</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk10 mtkb">##&nbsp;Usage</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">I&nbsp;have&nbsp;taken&nbsp;the&nbsp;data&nbsp;from&nbsp;this&nbsp;link&nbsp;:&nbsp;</span><span class="mtk1 detected-link">https://www.kaggle.com/datasets/manasgarg/ipl</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">In&nbsp;this&nbsp;link&nbsp;we&nbsp;don't&nbsp;have&nbsp;umpires&nbsp;region.&nbsp;I&nbsp;have&nbsp;</span><span class="mtk1">taken&nbsp;umpires&nbsp;region&nbsp;data&nbsp;from&nbsp;this&nbsp;link&nbsp;:&nbsp;</span><span class="mtk1 detected-link">https://</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1 detected-link">stats.espncricinfo.com/ci/engine/records/individua</span><span class="mtk1 detected-link">l/most_matches_umpire.html?id=117;type=trophy</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">You&nbsp;can&nbsp;directly&nbsp;download&nbsp;all&nbsp;the&nbsp;datasets&nbsp;from&nbsp;th</span><span class="mtk1">is&nbsp;repository&nbsp;as&nbsp;well.</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 114px; left: 125px; font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 886px; height: 12px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 12px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 886px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="500" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 500px;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 500px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 500px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 987px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; top: 114px; left: 213px; width: 1px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 987px;"><div class="accessibilityHelpWidget" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget" style="display: none; position: absolute;"><div role="document"></div></div><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 500px;"><div class="minimap-shadow-hidden" style="height: 500px;"></div><canvas width="0" height="500" style="position: absolute; left: 0px; width: 0px; height: 500px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="500" style="position: absolute; left: 0px; width: 0px; height: 500px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.modesContentHoverWidget" style="position: absolute; visibility: hidden; max-width: 1292px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-height: 250px; max-width: 651.42px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div><div class="monaco-editor rename-box" widgetid="__renameInputWidget" style="background-color: rgb(243, 243, 243); box-shadow: rgba(0, 0, 0, 0.16) 0px 0px 8px 2px; color: rgb(97, 97, 97); position: absolute; visibility: hidden; max-width: 1292px;"><input class="rename-input" type="text" aria-label="Rename input. Type new name and press Enter to commit." style="font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; background-color: rgb(255, 255, 255); border-width: 0px; border-style: none;"><div class="rename-label" style="font-size: 11.2px;">Enter to Rename, Shift+Enter to Preview</div></div></div><div class="context-view" aria-hidden="true" style="display: none;"></div></div></div>
<div class="js-edit-mode-pane hide" id="preview">
<div class="center">
<div class="gl-spinner-container" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-lg gl-spinner-dark gl-vertical-align-text-bottom!"></span></div>
</div>
</div>
</div>
</div>

<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-c8532b4a7277470636ad06585eaeb75c">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-c8532b4a7277470636ad06585eaeb75c" class="form-control gl-form-input js-commit-message" placeholder="Update README.md" data-qa-selector="commit_message_field" required="required" rows="3">Update README.md</textarea>
</div>
</div>
</div>

<div class="form-group row branch">
<label class="col-form-label col-sm-2" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="main" required="required" class="form-control gl-form-input js-branch-name ref-name">
<div class="js-create-merge-request-container" style="display: none;">
<div class="form-check gl-mt-3">
<input type="checkbox" name="create_merge_request" id="create_merge_request-3b09efc94561f7c456d7aaaa531e2a10" value="1" class="js-create-merge-request form-check-input" checked="checked">
<label class="form-check-label" for="create_merge_request-3b09efc94561f7c456d7aaaa531e2a10">Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="main" class="js-original-branch" autocomplete="off">

<input type="hidden" name="last_commit_sha" id="last_commit_sha" value="83687211f5907d1939ba01ff96b461dc61bc4cdc" autocomplete="off">
<input type="hidden" name="content" id="file-content" value="" autocomplete="off">
<input type="hidden" name="from_merge_request_iid" id="from_merge_request_iid" autocomplete="off">
<div class="form-actions gl-display-flex">
<button id="commit-changes" class="gl-button btn btn-md btn-confirm js-commit-button" data-qa-selector="commit_button" type="submit"><span class="gl-button-text">
Commit changes

</span>

</button><button class="gl-button btn btn-md btn-confirm js-commit-button-loading gl-display-none" aria-disabled="true" type="submit"><span class="gl-spinner-container gl-button-icon gl-button-loading-indicator" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-sm gl-spinner-dark gl-vertical-align-text-bottom!"></span></span>
<span class="gl-button-text">
Commit changes

</span>

</button><a class="gl-button btn btn-md btn-default gl-ml-3" id="cancel-changes" aria-label="Discard changes" data-confirm="Leave edit mode? All unsaved changes will be lost." data-confirm-btn-variant="danger" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/blob/main/README.md"><span class="gl-button-text">
Cancel

</span>

</a>
</div>

</form></div>

</main>
</div>


</div>
</div>
<div class="top-nav-responsive layout-page content-wrapper-margin">
<div class="cloak-startup">
<div><div data-testid="mobile-overlay" class="mobile-overlay"></div> <div><div class="gl-h-full gl-w-full"><div><header class="gl-display-flex gl-align-items-center gl-py-4 gl-pl-4"><h1 class="gl-m-0 gl-font-size-h2 gl-reset-color gl-mr-auto">Menu</h1> <a aria-label="Search" data-qa-selector="menu_item_link" data-qa-title="Search" href="https://gitlab.com/search?project_id=40954144" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-ml-3 btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="search-icon" role="img" aria-hidden="true" class="gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"></use></svg> <!----></span></span></a> <div class="dropdown b-dropdown gl-new-dropdown gl-ml-3 btn-group" no-caret="" data-qa-selector="mobile_new_dropdown" id="__BVID__83"><!----><button aria-haspopup="true" aria-expanded="false" type="button" class="btn dropdown-toggle btn-default btn-md top-nav-menu-item gl-button gl-dropdown-toggle btn-default-tertiary dropdown-icon-only dropdown-toggle-no-caret" id="__BVID__83__BV_toggle_"><!----> <svg data-testid="plus-icon" role="img" aria-hidden="true" class="dropdown-icon gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#plus"></use></svg> <span class="gl-new-dropdown-button-text gl-sr-only">Create new...</span> <svg data-testid="chevron-down-icon" role="img" aria-hidden="true" class="gl-button-icon dropdown-chevron gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"></use></svg></button><ul role="menu" tabindex="-1" class="dropdown-menu dropdown-menu-right" aria-labelledby="__BVID__83__BV_toggle_"><div class="gl-new-dropdown-inner"><!----> <!----> <div class="gl-new-dropdown-contents"><!----> <!----> <li role="presentation" class="gl-new-dropdown-section-header"><header data-testid="header" role="heading" class="dropdown-header">
      This project
    </header></li> <li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="new_issue_mobile_button" role="menuitem" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/issues/new" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        New issue
      </p> <!----></div> <!----></a></li><li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="new_merge request_mobile_button" role="menuitem" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/merge_requests/new" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        New merge request
      </p> <!----></div> <!----></a></li><li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="new_snippet_mobile_button" role="menuitem" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/snippets/new" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        New snippet
      </p> <!----></div> <!----></a></li><li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="invite_members_mobile_button" role="menuitem" href="https://gitlab.com/mountblue/cohort-22-python/manish/ipl-data-set-analytics/-/project_members" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        Invite members
      </p> <!----></div> <!----></a></li><li role="presentation" class="gl-new-dropdown-divider"><hr data-testid="divider" role="separator" aria-orientation="horizontal" class="dropdown-divider"></li> <li role="presentation" class="gl-new-dropdown-section-header"><header data-testid="header" role="heading" class="dropdown-header">
      GitLab
    </header></li> <li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="new_project/repository_mobile_button" role="menuitem" href="https://gitlab.com/projects/new" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        New project/repository
      </p> <!----></div> <!----></a></li><li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="new_group_mobile_button" role="menuitem" href="https://gitlab.com/groups/new" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        New group
      </p> <!----></div> <!----></a></li><li role="presentation" class="gl-new-dropdown-item"><a data-testid="item" data-qa-selector="new_snippet_mobile_button" role="menuitem" href="https://gitlab.com/-/snippets/new" target="_self" class="dropdown-item top-nav-menu-item"><!----> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary">
        New snippet
      </p> <!----></div> <!----></a></li></div> <!----></div></ul></div></header> <div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column gl-h-full"><div data-testid="menu-section" class=""><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block">
        Switch to
      </strong><button aria-label="Projects" data-track-label="projects_dropdown" data-track-action="click_dropdown" type="button" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary qa-projects-dropdown gl-mt-1" href="" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="project-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#project"></use></svg> 
      Projects
      <svg data-testid="chevron-right-icon" role="img" aria-hidden="true" class="gl-ml-auto gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-right"></use></svg></span></span></button><button aria-label="Groups" data-track-label="groups_dropdown" data-track-action="click_dropdown" type="button" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary qa-groups-dropdown gl-mt-1" href="" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="group-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#group"></use></svg> 
      Groups
      <svg data-testid="chevron-right-icon" role="img" aria-hidden="true" class="gl-ml-auto gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-right"></use></svg></span></span></button><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block gl-pt-3!">
        Explore
      </strong><a aria-label="Milestones" data-qa-selector="milestones_link" data-track-label="menu_milestones" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/milestones" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="clock-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#clock"></use></svg> 
      Milestones
      <!----></span></span></a><a aria-label="Snippets" data-qa-selector="snippets_link" data-track-label="menu_snippets" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/snippets" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="snippet-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#snippet"></use></svg> 
      Snippets
      <!----></span></span></a><a aria-label="Activity" data-qa-selector="activity_link" data-track-label="menu_activity" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/dashboard/activity" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="history-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#history"></use></svg> 
      Activity
      <!----></span></span></a><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block gl-pt-3!">
        Your dashboards
      </strong><a aria-label="Environments" data-qa-selector="environment_link" data-track-label="menu_environments" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/-/operations/environments" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="environment-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#environment"></use></svg> 
      Environments
      <!----></span></span></a><a aria-label="Operations" data-qa-selector="operations_link" data-track-label="menu_operations" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/-/operations" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="cloud-gear-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#cloud-gear"></use></svg> 
      Operations
      <!----></span></span></a><a aria-label="Security" data-qa-selector="security_link" data-track-label="menu_security" data-track-action="click_dropdown" data-track-property="navigation" href="https://gitlab.com/-/security/dashboard" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="shield-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#shield"></use></svg> 
      Security
      <!----></span></span></a></div></div></div></div></div></div>
</div>
</div>



<script nonce="">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.qa_selector = 'js_lazy_loaded_content';
  });
}

//]]>
</script>
<script nonce="">
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>




<div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><div><!----></div><div></div></body></html>