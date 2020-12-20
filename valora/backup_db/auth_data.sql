BEGIN;
INSERT INTO "auth_user_groups" ("id","user_id","group_id") VALUES 
( 1, 2, 1 ),
( 2, 3, 1 ),
( 3, 4, 1 ),
( 4, 4, 2 );
COMMIT;

BEGIN;
INSERT INTO "auth_group_permissions" ("id","group_id","permission_id") VALUES 
( 1, 1, 64 ),
( 2, 1, 68 ),
( 3, 1, 69 ),
( 4, 1, 70 ),
( 5, 1, 72 ),
( 6, 1, 60 ),
( 7, 2, 64 ),
( 8, 2, 65 ),
( 9, 2, 66 ),
( 10, 2, 67 ),
( 11, 2, 68 ),
( 12, 2, 69 ),
( 13, 2, 70 ),
( 14, 2, 71 ),
( 15, 2, 72 ),
( 16, 2, 57 ),
( 17, 2, 58 ),
( 18, 2, 59 ),
( 19, 2, 60 ),
( 20, 2, 61 ),
( 21, 2, 62 ),
( 22, 2, 63 );
COMMIT;

BEGIN;
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES 
( 1, 'pbkdf2_sha256$216000$q0vnse0d2iWU$ayGOsrojojh12SVwVIbUHap3t3wEEapKbaOyoRjt9cQ=', '2020-12-20 15:19:03.014783', 1, 'luigus', '', '', 1, 1, '2020-12-20 15:18:34.546756', '' ),
( 2, 'pbkdf2_sha256$216000$Bia65yiRCN1z$NuWfRfnHNJVnSulbx8qKIf4GK2dPtCtgqfhSYGvQBRE=', NULL, 0, 'player1', '', '', 0, 1, '2020-12-20 15:25:39', '' ),
( 3, 'pbkdf2_sha256$216000$GTU9yoEgzf3U$ZybeWjaM8KqPAK5Zz8u4iu5ST09Z+nSZgJcLM5h7DwA=', NULL, 0, 'player2', '', '', 0, 1, '2020-12-20 15:26:12', '' ),
( 4, 'pbkdf2_sha256$216000$zFXX5eJBoMTe$YeEnUZ9Y8eF1FWkP0ezTg1mFNAG4mdWFAptnDHlVyBw=', NULL, 0, 'admin', '', '', 0, 1, '2020-12-20 15:26:38', '' );
COMMIT;


BEGIN;
INSERT INTO "auth_group" ("id","name") VALUES 
( 1, 'Player' ),
( 2, 'Admin' );
COMMIT;

