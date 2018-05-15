export DEBIAN_FRONTEND=noninteractive
debconf-set-selections <<EOF
slapd slapd/internal/generate_adminpw password $2
slapd slapd/password2 password $2
slapd slapd/internal/adminpw password $2
slapd slapd/password1 password $2
slapd slapd/domain string $1
slapd shares/organization string $1
EOF