NAME = iprediaos-profile-firefox

VERSION := $(shell awk '/Version:/ { print $$2 }' $(NAME).spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' $(NAME).spec | sed 's|%{?dist}||g')
TAG=$(NAME)-$(VERSION)-$(RELEASE)

tag:
	@git tag -a -f -m "Tag as $(TAG)" -f $(TAG)
	@echo "Tagged as $(TAG)"

install:
	@install -D etc/skel/.mozilla/firefox/profiles.ini ${DESTDIR}/etc/skel/.mozilla/firefox/profiles.ini
	@install -D etc/skel/.mozilla/firefox/a.default/user.js ${DESTDIR}/etc/skel/.mozilla/firefox/a.default/user.js

archive: tag
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD > $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"

clean:
	rm -f *~ *bz2
