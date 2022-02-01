EXTRA_DIST = \
	Levuaska \
	COPYING \
	AUTHORS \
	README.md

themedir = $(datadir)/themes

install-data-hook:
	$(MKDIR_P) $(DESTDIR)/usr/share/themes
	cp -Rv Levuaska $(DESTDIR)/usr/share/themes/.

uninstall-hook:
	test -e $(DESTDIR)/usr/share/themes/Levuaska && rm -rfv $(DESTDIR)/usr/share/themes/Levuaska
