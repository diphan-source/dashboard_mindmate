import React from "react";

const Sidebar = () => {
	return (
		<div>
			<div class="logo-wrapper">
				<a href="index_2.html">
					<img
						class="img-fluid for-light"
						src="../assets/images/logo/small-logo_2.png"
						alt=""
					/>
					<img
						class="img-fluid for-dark"
						src="../assets/images/logo/small-white-logo_2.png"
						alt=""
					/>
				</a>
				<div class="back-btn">
					<i class="fa fa-angle-left"></i>
				</div>
			</div>
			<div class="logo-icon-wrapper">
				<a href="index_2.html">
					<img
						class="img-fluid"
						src="../assets/images/logo-icon_2.png"
						alt=""
					/>
				</a>
			</div>
			<nav class="sidebar-main">
				<div class="left-arrow disabled" id="left-arrow">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="24"
						height="24"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
						class="feather feather-arrow-left">
						<line x1="19" y1="12" x2="5" y2="12"></line>
						<polyline points="12 19 5 12 12 5"></polyline>
					</svg>
				</div>
				<div id="sidebar-menu">
					<ul
						class="sidebar-links"
						id="simple-bar"
						data-simplebar="init"
						style="display: block;">
						<div
							class="simplebar-wrapper"
							style="margin: 0px;">
							<div class="simplebar-height-auto-observer-wrapper">
								<div class="simplebar-height-auto-observer"></div>
							</div>
							<div class="simplebar-mask">
								<div
									class="simplebar-offset"
									style="right: 0px; bottom: 0px;">
									<div
										class="simplebar-content-wrapper"
										style="height: 100%; overflow: hidden scroll;">
										<div
											class="simplebar-content"
											style="padding: 0px;">
											<li class="back-btn">
												<a
													href="index_2.html"
													class="active">
													<img
														class="img-fluid"
														src="../assets/images/logo-icon_2.png"
														alt=""
													/>
												</a>
												<div class="mobile-back text-end">
													<span>Back</span>
													<i
														class="fa fa-angle-right ps-2"
														aria-hidden="true"></i>
												</div>
											</li>
											<li class="sidebar-list">
												<a
													class="sidebar-link sidebar-title"
													href="../theme/index_2.html">
													<svg
														xmlns="http://www.w3.org/2000/svg"
														width="24"
														height="24"
														viewBox="0 0 24 24"
														fill="none"
														stroke="currentColor"
														stroke-width="2"
														stroke-linecap="round"
														stroke-linejoin="round"
														class="feather feather-home">
														<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
														<polyline points="9 22 9 12 15 12 15 22"></polyline>
													</svg>
													<span>Dashboard </span>
													<div class="according-menu">
														<i class="fa fa-angle-right"></i>
													</div>
												</a>
											</li>
											<li class="sidebar-list">
												<a
													class="sidebar-link sidebar-title active"
													href="index_2.html#">
													<svg
														xmlns="http://www.w3.org/2000/svg"
														width="24"
														height="24"
														viewBox="0 0 24 24"
														fill="none"
														stroke="currentColor"
														stroke-width="2"
														stroke-linecap="round"
														stroke-linejoin="round"
														class="feather feather-anchor">
														<circle
															cx="12"
															cy="5"
															r="3"></circle>
														<line
															x1="12"
															y1="22"
															x2="12"
															y2="8"></line>
														<path d="M5 12H2a10 10 0 0 0 20 0h-3"></path>
													</svg>
													<span>Starter kit</span>
													<div class="according-menu">
														<i class="fa fa-angle-down"></i>
													</div>
												</a>
												<ul
													class="sidebar-submenu"
													style="display: block;">
													<li>
														<a
															class="submenu-title"
															href="index_2.html#">
															color version
															<span class="sub-arrow">
																<i class="fa fa-chevron-right"></i>
															</span>
															<div class="according-menu">
																<i class="fa fa-angle-right"></i>
															</div>
														</a>
														<ul
															class="nav-sub-childmenu submenu-content"
															style="display: none;">
															<li>
																<a
																	href="index_2.html"
																	class="active">
																	Layout Light
																</a>
															</li>
															<li>
																<a href="layout-dark_2.html">
																	Layout Dark
																</a>
															</li>
														</ul>
													</li>
													<li>
														{" "}
														<a
															class="submenu-title"
															href="index_2.html#">
															Page layout
															<span class="sub-arrow">
																<i class="fa fa-chevron-right"></i>
															</span>
															<div class="according-menu">
																<i class="fa fa-angle-right"></i>
															</div>
														</a>
														<ul
															class="nav-sub-childmenu submenu-content"
															style="display: none;">
															<li>
																<a href="boxed_2.html">
																	Boxed
																</a>
															</li>
															<li>
																<a href="layout-rtl_2.html">
																	RTL
																</a>
															</li>
														</ul>
													</li>
													<li>
														{" "}
														<a
															class="submenu-title"
															href="index_2.html#">
															Footers
															<span class="sub-arrow">
																<i class="fa fa-chevron-right"></i>
															</span>
															<div class="according-menu">
																<i class="fa fa-angle-right"></i>
															</div>
														</a>
														<ul
															class="nav-sub-childmenu submenu-content"
															style="display: none;">
															<li>
																<a href="footer-light_2.html">
																	Footer Light
																</a>
															</li>
															<li>
																<a href="footer-dark_2.html">
																	Footer Dark
																</a>
															</li>
															<li>
																<a href="footer-fixed_2.html">
																	Footer Fixed
																</a>
															</li>
														</ul>
													</li>
												</ul>
											</li>
											<li class="sidebar-list">
												<a
													class="sidebar-link sidebar-title"
													href="http://support.pixelstrap.com/help-center"
													target="_blank">
													<svg
														xmlns="http://www.w3.org/2000/svg"
														width="24"
														height="24"
														viewBox="0 0 24 24"
														fill="none"
														stroke="currentColor"
														stroke-width="2"
														stroke-linecap="round"
														stroke-linejoin="round"
														class="feather feather-headphones">
														<path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
														<path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
													</svg>
													<span>Raise Support</span>
													<div class="according-menu">
														<i class="fa fa-angle-right"></i>
													</div>
												</a>
											</li>
											<li class="sidebar-list">
												<a
													class="sidebar-link sidebar-title"
													href="http://admin.pixelstrap.com/zeta/document/index.html"
													target="_blank">
													<svg
														xmlns="http://www.w3.org/2000/svg"
														width="24"
														height="24"
														viewBox="0 0 24 24"
														fill="none"
														stroke="currentColor"
														stroke-width="2"
														stroke-linecap="round"
														stroke-linejoin="round"
														class="feather feather-file-text">
														<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
														<polyline points="14 2 14 8 20 8"></polyline>
														<line
															x1="16"
															y1="13"
															x2="8"
															y2="13"></line>
														<line
															x1="16"
															y1="17"
															x2="8"
															y2="17"></line>
														<polyline points="10 9 9 9 8 9"></polyline>
													</svg>
													<span>Documentation </span>
													<div class="according-menu">
														<i class="fa fa-angle-right"></i>
													</div>
												</a>
											</li>
										</div>
									</div>
								</div>
							</div>
							<div
								class="simplebar-placeholder"
								style="width: auto; height: 307px;"></div>
						</div>
						<div
							class="simplebar-track simplebar-horizontal"
							style="visibility: hidden;">
							<div
								class="simplebar-scrollbar"
								style="width: 0px; display: none;"></div>
						</div>
						<div
							class="simplebar-track simplebar-vertical"
							style="visibility: visible;">
							<div
								class="simplebar-scrollbar"
								style="height: 607px; display: block; transform: translate3d(0px, 0px, 0px);"></div>
						</div>
					</ul>
					<div class="sidebar-img-section">
						<div class="sidebar-img-content">
							<img
								class="img-fluid"
								src="../assets/images/side-bar_2.png"
								alt=""
							/>
							<h4>Need Help ?</h4>
							<a
								class="txt"
								href="https://pixelstrap.freshdesk.com/support/home">
								Raise ticket at "support@pixelstrap.com"
							</a>
							<a
								class="btn btn-secondary"
								href="https://themeforest.net/user/pixelstrap/portfolio">
								Buy Now
							</a>
						</div>
					</div>
				</div>
			</nav>
		</div>
	);
};

export default Sidebar;
