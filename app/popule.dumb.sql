BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	char(32) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag">=0),
	FOREIGN KEY("user_id") REFERENCES "core_usermodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_categoryquestionmodel" (
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"id"	char(32) NOT NULL,
	"category_id"	char(32) NOT NULL,
	"question_id"	char(32) NOT NULL,
	FOREIGN KEY("question_id") REFERENCES "core_questionmodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "core_categorymodel"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "core_rankingmodel" (
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"id"	char(32) NOT NULL,
	"value"	integer NOT NULL,
	"category_id"	char(32) NOT NULL,
	"user_id"	char(32) NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "core_usermodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "core_categorymodel"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "core_answermodel" (
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"id"	char(32) NOT NULL,
	"answer"	varchar(200) NOT NULL,
	"correct_answer"	bool NOT NULL,
	"question_id"	char(32) NOT NULL,
	FOREIGN KEY("question_id") REFERENCES "core_questionmodel"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "core_questionmodel" (
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"id"	char(32) NOT NULL,
	"question"	varchar(200) NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "core_categorymodel" (
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"id"	char(32) NOT NULL,
	"name"	varchar(200) NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "core_usermodel_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"usermodel_id"	char(32) NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("usermodel_id") REFERENCES "core_usermodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_usermodel_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"usermodel_id"	char(32) NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("usermodel_id") REFERENCES "core_usermodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_usermodel" (
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(150) NOT NULL,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"id"	char(32) NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('155binx8augzbmlt9yulzkmrfjxiawyf','.eJxVzMsOwiAQheF3YS0kMDCAS_c-QzMDg62aNullZXx3bdKFrs__nZfqaFv7bltk7oaqzoprZE8etACI9g5Rc6hVF07RR7TMVtTplzGVh4y7rXcab5Mp07jOA5s9Mce6mOtU5Xk52r-Dnpb-qwvGaNG3QC4lykwhYBAuFNklSNAcB8olcm7kAG2VlrK3VjCDMIp6fwAyXkG6:1mN1qJ:_T_dwKymnIu1zAMge-6Nf4Q20v1vcWAFPsmQ2Hjf-C4','2021-09-19 23:46:31.978866');
INSERT INTO "django_admin_log" ("id","action_time","object_id","object_repr","change_message","content_type_id","user_id","action_flag") VALUES (1,'2021-09-05 15:24:21.413077','de53151d-8046-4188-8799-626e986ab3b2','MATEMÁTICA','[{"added": {}}]',7,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (2,'2021-09-05 15:26:07.018206','a6b2086c-021c-4a03-aff1-fe7300fcd190','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (3,'2021-09-05 15:26:19.051548','1847b6bc-241e-43fd-8b83-b2dc1f2d2e62','Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltiplos do número','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (4,'2021-09-05 15:26:59.595235','bd7f1983-9216-437e-9237-7aeacdf5abbf','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (5,'2021-09-05 15:27:15.521839','6b10d83d-8a8f-4851-bfe8-250e8f4791ef','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (6,'2021-09-05 15:27:24.835840','584ccbab-6a06-43c6-903f-b3ee9f7f2c53','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (7,'2021-09-05 15:27:40.270577','e9b3ea5e-a779-4345-8116-acc0dc9d5b43','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (8,'2021-09-05 15:27:51.271034','af036eaf-039a-4603-9a6c-84bc3b1c70ff','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (9,'2021-09-05 15:28:22.433782','4334b327-3e97-40c1-8869-25ab22381df5','Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltiplos do número ','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (10,'2021-09-05 15:28:36.934161','adc27240-2133-4dda-bb73-d0b8228af4b7','Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltiplos do número ','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (11,'2021-09-05 15:28:47.952541','c80a9ca7-e8d6-4e25-a86b-e22e3dc2e3c8','Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltiplos do número ','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (12,'2021-09-05 15:29:18.121272','78692d51-2703-428f-bdca-55b2fd1bc5b5','Matemática - Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em jan','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (13,'2021-09-05 15:29:24.089858','c22ed16d-d2f5-4a09-897a-97287af3690a','Matemática - Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltipl','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (14,'2021-09-05 15:29:34.606238','99cd235f-e77c-47d5-8d90-fd512475d6a3','GERAL','[{"added": {}}]',7,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (15,'2021-09-05 15:29:44.056918','40d36491-6208-413e-8623-45eb7e0d3ac9','Geral - Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro.','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (16,'2021-09-05 15:29:49.929661','923ee893-3c7d-4b5b-a927-616986217044','Geral - Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltiplos do','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (17,'2021-09-05 15:30:27.780586','bd7b4a43-e33e-4266-b5dd-cb874761bb1e','admin','[{"changed": {"fields": ["First name", "Last name"]}}]',6,'bd7b4a43e33e4266b5ddcb874761bb1e',2),
 (18,'2021-09-05 15:30:47.629391','6619b888-dc2f-4d8f-9ce0-445da5a418c3','bruno','[{"added": {}}]',6,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (19,'2021-09-05 15:31:08.689274','6619b888-dc2f-4d8f-9ce0-445da5a418c3','bruno','[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]',6,'bd7b4a43e33e4266b5ddcb874761bb1e',2),
 (20,'2021-09-05 15:51:24.433803','1','player','[{"added": {}}]',3,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (21,'2021-09-05 21:37:49.592236','b3f05f58-b18b-43d9-853f-31aaf18014bf','brunoalmeidamartins','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (22,'2021-09-05 21:37:49.596532','ebfc0bd0-e8be-4f28-98f7-3f82f4ab9d1f','brunoalmeidamartins10','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (23,'2021-09-05 21:37:49.599040','349fa086-46cb-4769-abf8-05648df28342','brunoalmeidamartins11','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (24,'2021-09-05 21:37:49.601775','0e3a69e5-c101-452e-9f7a-5224f1d77ee7','brunoalmeidamartins2','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (25,'2021-09-05 21:37:49.605011','a7ec0456-032b-4bfb-8611-0b2018b2d269','brunoalmeidamartins3','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (26,'2021-09-05 21:37:49.607871','f6d61349-ee0d-49cd-b688-1cae91dec568','brunoalmeidamartins4','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (27,'2021-09-05 21:37:49.610665','9bb8b70d-ee55-4aef-8635-e5ee77806e4c','brunoalmeidamartins5','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (28,'2021-09-05 21:37:49.613604','c2633a12-c262-407e-97d6-7a942038d7ea','brunoalmeidamartins6','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (29,'2021-09-05 21:37:49.616411','57e401a1-d7f5-4466-8ac9-d402e48ec6e6','brunoalmeidamartins7','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (30,'2021-09-05 21:37:49.619235','85232bd5-ff51-41d2-ba93-b554b4fa85e1','brunoalmeidamartins8','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (31,'2021-09-05 21:37:49.622038','8f165e7c-55e0-40d9-99bb-4c1451fea04d','brunoalmeidamartins9','',6,'bd7b4a43e33e4266b5ddcb874761bb1e',3),
 (32,'2021-09-05 21:43:47.988707','c15241a5-07e4-4815-8540-f3abb60b8e88','TESTE','[{"added": {}}]',7,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (33,'2021-09-05 21:43:57.128492','ddfba6ba-cb9f-4314-8c86-f565e8cf64b0','TESTE2','[{"added": {}}]',7,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (34,'2021-09-05 22:14:56.356657','6619b888-dc2f-4d8f-9ce0-445da5a418c3','bruno','[{"changed": {"fields": ["password"]}}]',6,'bd7b4a43e33e4266b5ddcb874761bb1e',2),
 (35,'2021-09-05 23:29:12.417142','40cb7abf-fd13-41dc-959d-e9e59a587dd7','Carlos deu 85 bombons para João e ficou com 415. Quantos bombons tinha Carlos?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (36,'2021-09-05 23:29:21.061225','50baf93b-8902-447d-98d9-5f3b94e87f1f','Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (37,'2021-09-05 23:29:28.493742','a60ed825-c1e0-4cff-8807-11de63f07f86','Na confeitaria tinha 400 ovos, foram comprados mais 9 dúzias e foram usados 279. Quantos ovos restaram?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (38,'2021-09-05 23:29:35.620011','e52b2c09-23d3-46e5-b3d1-7af62f05536c','No restaurante foram servidos 500 almoços, 237 jantares e cada refeição foi dado uma sobremesa de cortesia. Quantas sobremesas foram dadas?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (39,'2021-09-05 23:29:44.869041','843a781d-6e88-49b7-8c2a-f4b77871b2a1','Numa pasta tem 3 arquivos de documentos, o 2º arquivo tem 1.675 e o 3º arquivo tem 1.394,o total de 3.858. Quantos documentos têm no 1º arquivo?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (40,'2021-09-05 23:29:52.553418','8019b72a-f5bf-4d27-b3b3-659d3186956e','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (41,'2021-09-05 23:31:07.336725','a87c64a1-121f-4004-abb1-790e4522b8b6','33 * 45 ?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (42,'2021-09-05 23:31:19.369091','208ada0e-9f97-4231-8cc0-eab886e3ab9e','45 * 789?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (43,'2021-09-05 23:31:32.110685','2ad79a31-abd4-402c-b38e-aa4a1ed00946','145 / 5?','[{"added": {}}]',8,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (44,'2021-09-05 23:32:19.122144','269ca84b-55ff-4db3-a5f7-d825e5f75062','33 * 45 ? 1485','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (45,'2021-09-05 23:32:28.406366','36d18829-ec87-4c2b-9daf-d006ff7201f7','33 * 45 ? 1458','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (46,'2021-09-05 23:32:46.573104','9722a76f-43ff-4980-9f58-7b3a256dbc1e','33 * 45 ? 1483','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (47,'2021-09-05 23:33:10.716515','37fab49e-edc7-4e53-ac49-9788d12e7cc5','45 * 789? 35505','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (48,'2021-09-05 23:33:19.974527','71769ce1-b260-4475-b266-76307c672efa','45 * 789? 35506','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (49,'2021-09-05 23:33:29.674237','02a787cf-c7c8-4a09-8a79-3a2a9a56c082','45 * 789? 35502','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (50,'2021-09-05 23:33:43.060340','be74b1de-aeca-4683-b7d3-a4c64f4df1b8','145 / 5? 29','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (51,'2021-09-05 23:33:52.927168','a5fc9486-1005-4aee-ba03-b9209a0fea80','145 / 5? 30','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (52,'2021-09-05 23:33:59.607629','4f756714-3dab-4677-87ce-d479b80d94f8','145 / 5? 28','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (53,'2021-09-05 23:35:00.292664','881c0992-1844-483c-9ec0-a33cbd9fde40','Carlos deu 85 bombons para João e ficou com 415. Quantos bombons tinha Carlos? 500','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (54,'2021-09-05 23:35:07.575267','6041f2b6-680c-474c-83ea-59a337da9aab','Carlos deu 85 bombons para João e ficou com 415. Quantos bombons tinha Carlos? 501','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (55,'2021-09-05 23:35:14.454579','a7eb2c1e-5564-43e0-8877-984578ccfd7a','Carlos deu 85 bombons para João e ficou com 415. Quantos bombons tinha Carlos? 505','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (56,'2021-09-05 23:35:51.384811','c3391192-ca23-4143-8e59-6e486cd30eda','Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo? 141','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (57,'2021-09-05 23:36:30.176763','a702b2ba-d855-4c5e-941a-68f0b63092e0','Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo? 458','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (58,'2021-09-05 23:36:59.565251','c3391192-ca23-4143-8e59-6e486cd30eda','Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo? 659','[{"changed": {"fields": ["Resposta"]}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',2),
 (59,'2021-09-05 23:37:13.897582','431df3b8-7001-436e-ac9b-d557f3675cfb','Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo? 660','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (60,'2021-09-05 23:37:49.217736','b939c122-0c1d-4dc9-af96-476267bb6965','Na confeitaria tinha 400 ovos, foram comprados mais 9 dúzias e foram usados 279. Quantos ovos restaram? 229','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (61,'2021-09-05 23:37:56.782728','b99b4d09-dc5b-45cf-b829-ca4e1d17d43d','Na confeitaria tinha 400 ovos, foram comprados mais 9 dúzias e foram usados 279. Quantos ovos restaram? 300','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (62,'2021-09-05 23:38:05.280831','9d301d29-d79c-4aa2-808b-504b19b536f8','Na confeitaria tinha 400 ovos, foram comprados mais 9 dúzias e foram usados 279. Quantos ovos restaram? 228','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (63,'2021-09-05 23:38:31.557053','ad724cdf-7db4-4a48-8d41-a7be3e214cb8','No restaurante foram servidos 500 almoços, 237 jantares e cada refeição foi dado uma sobremesa de cortesia. Quantas sobremesas foram dadas? 737','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (64,'2021-09-05 23:38:42.171770','67170dc8-d812-4335-b90e-4e4b2eb5e2b4','No restaurante foram servidos 500 almoços, 237 jantares e cada refeição foi dado uma sobremesa de cortesia. Quantas sobremesas foram dadas? 738','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (65,'2021-09-05 23:38:57.182897','873478c5-81b3-4cde-afde-bec4b68d6212','No restaurante foram servidos 500 almoços, 237 jantares e cada refeição foi dado uma sobremesa de cortesia. Quantas sobremesas foram dadas? 736','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (66,'2021-09-05 23:39:41.307676','30f2ced3-3af5-4962-b8f5-902f85d2a993','Numa pasta tem 3 arquivos de documentos, o 2º arquivo tem 1.675 e o 3º arquivo tem 1.394,o total de 3.858. Quantos documentos têm no 1º arquivo? 789','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (67,'2021-09-05 23:39:48.664472','442415a6-cf22-425d-9f94-48b9c027c9f0','Numa pasta tem 3 arquivos de documentos, o 2º arquivo tem 1.675 e o 3º arquivo tem 1.394,o total de 3.858. Quantos documentos têm no 1º arquivo? 790','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (68,'2021-09-05 23:39:55.553739','95b95663-a505-48ba-aefb-dda64a548441','Numa pasta tem 3 arquivos de documentos, o 2º arquivo tem 1.675 e o 3º arquivo tem 1.394,o total de 3.858. Quantos documentos têm no 1º arquivo? 787','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (69,'2021-09-05 23:40:35.966226','7ed1c4ef-4079-4e5e-9cb0-e995fee8afda','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo? 6393','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (70,'2021-09-05 23:42:13.038418','7ed1c4ef-4079-4e5e-9cb0-e995fee8afda','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo? 6393','[]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',2),
 (71,'2021-09-05 23:42:23.907239','674ef408-e105-46e4-9f4d-4b47912a7f2b','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo? 6394','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (72,'2021-09-05 23:42:31.003629','e5ebeedf-d833-4b22-88f9-3d960c3ae3f1','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo? 6395','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (73,'2021-09-05 23:42:41.892538','9423fff8-84d7-4bf7-b467-25613a5385eb','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo? 6347','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (74,'2021-09-05 23:42:51.461580','7c9e6ea7-997a-43a2-aee4-00ec71602bb6','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo? 6400','[{"added": {}}]',9,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (75,'2021-09-05 23:43:07.415078','9cefd33a-472c-4dd4-86d5-f2c6ef581672','Matemática - Carlos deu 85 bombons para João e ficou com 415. Quantos bombons tinha Carlos?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (76,'2021-09-05 23:43:11.356276','15314301-f27f-4713-a632-5622af826d71','Matemática - Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (77,'2021-09-05 23:43:19.105623','8e803fda-0925-460b-aea3-fadfadc797ef','Matemática - Na confeitaria tinha 400 ovos, foram comprados mais 9 dúzias e foram usados 279. Quantos ovos restaram?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (78,'2021-09-05 23:43:29.997789','688b4fcc-78f0-4a08-a981-e2a788ee2c80','Matemática - No restaurante foram servidos 500 almoços, 237 jantares e cada refeição foi dado uma sobremesa de cortesia. Quantas sobremesas foram dadas?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (79,'2021-09-05 23:43:35.424355','f5993c15-3192-444d-8284-119c1a62be82','Matemática - Numa pasta tem 3 arquivos de documentos, o 2º arquivo tem 1.675 e o 3º arquivo tem 1.394,o total de 3.858. Quantos documentos têm no 1º arquivo?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (80,'2021-09-05 23:43:39.598376','eede442d-318d-4361-97f1-3a3a35edc57c','Matemática - A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (81,'2021-09-05 23:43:43.709667','f4e1fc16-b093-4645-a56d-c976498a114c','Matemática - 33 * 45 ?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (82,'2021-09-05 23:43:47.481527','4d14d1c6-6107-48cd-a854-0fc883a66070','Matemática - 45 * 789?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1),
 (83,'2021-09-05 23:43:54.397365','4aa51250-f182-430d-bbc5-ac0acf56e63c','Matemática - 145 / 5?','[{"added": {}}]',11,'bd7b4a43e33e4266b5ddcb874761bb1e',1);
INSERT INTO "core_categoryquestionmodel" ("created_at","updated_at","id","category_id","question_id") VALUES ('2021-09-05 15:29:18.120580','2021-09-05 15:29:18.120649','78692d512703428fbdca55b2fd1bc5b5','de53151d804641888799626e986ab3b2','a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:29:24.089403','2021-09-05 15:29:24.089433','c22ed16dd2f54a09897a97287af3690a','de53151d804641888799626e986ab3b2','1847b6bc241e43fd8b83b2dc1f2d2e62'),
 ('2021-09-05 15:29:44.056239','2021-09-05 15:29:44.056269','40d364916208413e862345eb7e0d3ac9','99cd235fe77c47d58d90fd512475d6a3','a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:29:49.929235','2021-09-05 15:29:49.929260','923ee8933c7d4b5ba927616986217044','99cd235fe77c47d58d90fd512475d6a3','1847b6bc241e43fd8b83b2dc1f2d2e62'),
 ('2021-09-05 23:43:07.414490','2021-09-05 23:43:07.414512','9cefd33a472c4dd486d5f2c6ef581672','de53151d804641888799626e986ab3b2','40cb7abffd1341dc959de9e59a587dd7'),
 ('2021-09-05 23:43:11.355768','2021-09-05 23:43:11.355800','15314301f27f4713a6325622af826d71','de53151d804641888799626e986ab3b2','50baf93b8902447d98d95f3b94e87f1f'),
 ('2021-09-05 23:43:19.104742','2021-09-05 23:43:19.104777','8e803fda0925460baea3fadfadc797ef','de53151d804641888799626e986ab3b2','a60ed825c1e04cff880711de63f07f86'),
 ('2021-09-05 23:43:29.997298','2021-09-05 23:43:29.997323','688b4fcc78f04a08a981e2a788ee2c80','de53151d804641888799626e986ab3b2','e52b2c0923d346e5b3d17af62f05536c'),
 ('2021-09-05 23:43:35.423301','2021-09-05 23:43:35.423409','f5993c153192444d8284119c1a62be82','de53151d804641888799626e986ab3b2','843a781d6e8849b78c2af4b77871b2a1'),
 ('2021-09-05 23:43:39.597984','2021-09-05 23:43:39.598007','eede442d318d436197f13a3a35edc57c','de53151d804641888799626e986ab3b2','8019b72af5bf4d27b3b3659d3186956e'),
 ('2021-09-05 23:43:43.709259','2021-09-05 23:43:43.709284','f4e1fc16b0934645a56dc976498a114c','de53151d804641888799626e986ab3b2','a87c64a1121f4004abb1790e4522b8b6'),
 ('2021-09-05 23:43:47.481135','2021-09-05 23:43:47.481159','4d14d1c6610748cda8540fc883a66070','de53151d804641888799626e986ab3b2','208ada0e9f9742318cc0eab886e3ab9e'),
 ('2021-09-05 23:43:54.396954','2021-09-05 23:43:54.396982','4aa51250f182430dbbc5ac0acf56e63c','de53151d804641888799626e986ab3b2','2ad79a31abd4402cb38eaa4a1ed00946');
INSERT INTO "core_rankingmodel" ("created_at","updated_at","id","value","category_id","user_id") VALUES ('2021-09-05 19:56:59.695884','2021-09-06 00:00:54.966281','7103e05d396843c8ab3e9ce609b81c2f',10,'de53151d804641888799626e986ab3b2','6619b888dc2f4d8f9ce0445da5a418c3');
INSERT INTO "core_answermodel" ("created_at","updated_at","id","answer","correct_answer","question_id") VALUES ('2021-09-05 15:26:59.594423','2021-09-05 15:26:59.594457','bd7f19839216437e92377aeacdf5abbf','14909',0,'a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:27:15.521190','2021-09-05 15:27:15.521228','6b10d83d8a8f4851bfe8250e8f4791ef','27476',1,'a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:27:24.834886','2021-09-05 15:27:24.834936','584ccbab6a0643c6903fb3ee9f7f2c53','16753',0,'a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:27:40.270153','2021-09-05 15:27:40.270180','e9b3ea5ea77943458116acc0dc9d5b43','9754',0,'a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:27:51.269977','2021-09-05 15:27:51.270023','af036eaf039a46039a6c84bc3b1c70ff','25897',0,'a6b2086c021c4a03aff1fe7300fcd190'),
 ('2021-09-05 15:28:22.432874','2021-09-05 15:28:22.432919','4334b3273e9740c1886925ab22381df5','14',0,'1847b6bc241e43fd8b83b2dc1f2d2e62'),
 ('2021-09-05 15:28:36.933346','2021-09-05 15:28:36.933404','adc2724021334ddabb73d0b8228af4b7','35',1,'1847b6bc241e43fd8b83b2dc1f2d2e62'),
 ('2021-09-05 15:28:47.951922','2021-09-05 15:28:47.951944','c80a9ca7e8d64e25a86be22e3dc2e3c8','20',0,'1847b6bc241e43fd8b83b2dc1f2d2e62'),
 ('2021-09-05 23:32:19.121175','2021-09-05 23:32:19.121218','269ca84b55ff4db3a5f7d825e5f75062','1485',1,'a87c64a1121f4004abb1790e4522b8b6'),
 ('2021-09-05 23:32:28.405592','2021-09-05 23:32:28.405635','36d18829ec874c2b9dafd006ff7201f7','1458',0,'a87c64a1121f4004abb1790e4522b8b6'),
 ('2021-09-05 23:32:46.572318','2021-09-05 23:32:46.572366','9722a76f43ff49809f587b3a256dbc1e','1483',0,'a87c64a1121f4004abb1790e4522b8b6'),
 ('2021-09-05 23:33:10.715925','2021-09-05 23:33:10.715974','37fab49eedc74e53ac499788d12e7cc5','35505',1,'208ada0e9f9742318cc0eab886e3ab9e'),
 ('2021-09-05 23:33:19.973154','2021-09-05 23:33:19.973262','71769ce1b2604475b26676307c672efa','35506',0,'208ada0e9f9742318cc0eab886e3ab9e'),
 ('2021-09-05 23:33:29.673237','2021-09-05 23:33:29.673280','02a787cfc7c84a098a793a2a9a56c082','35502',0,'208ada0e9f9742318cc0eab886e3ab9e'),
 ('2021-09-05 23:33:43.059760','2021-09-05 23:33:43.059810','be74b1deaeca4683b7d3a4c64f4df1b8','29',1,'2ad79a31abd4402cb38eaa4a1ed00946'),
 ('2021-09-05 23:33:52.926476','2021-09-05 23:33:52.926518','a5fc948610054aeeba03b9209a0fea80','30',0,'2ad79a31abd4402cb38eaa4a1ed00946'),
 ('2021-09-05 23:33:59.606658','2021-09-05 23:33:59.606722','4f7567143dab467787ced479b80d94f8','28',0,'2ad79a31abd4402cb38eaa4a1ed00946'),
 ('2021-09-05 23:35:00.292264','2021-09-05 23:35:00.292288','881c09921844483c9ec0a33cbd9fde40','500',1,'40cb7abffd1341dc959de9e59a587dd7'),
 ('2021-09-05 23:35:07.574360','2021-09-05 23:35:07.574409','6041f2b6680c474c83ea59a337da9aab','501',0,'40cb7abffd1341dc959de9e59a587dd7'),
 ('2021-09-05 23:35:14.454164','2021-09-05 23:35:14.454191','a7eb2c1e556443e08877984578ccfd7a','505',0,'40cb7abffd1341dc959de9e59a587dd7'),
 ('2021-09-05 23:35:51.384299','2021-09-05 23:36:59.564711','c3391192ca2341438e596e486cd30eda','659',1,'50baf93b8902447d98d95f3b94e87f1f'),
 ('2021-09-05 23:36:30.176327','2021-09-05 23:36:30.176355','a702b2bad8554c5e941a68f0b63092e0','458',0,'50baf93b8902447d98d95f3b94e87f1f'),
 ('2021-09-05 23:37:13.897182','2021-09-05 23:37:13.897207','431df3b87001436eac9bd557f3675cfb','660',0,'50baf93b8902447d98d95f3b94e87f1f'),
 ('2021-09-05 23:37:49.217313','2021-09-05 23:37:49.217336','b939c1220c1d4dc9af96476267bb6965','229',1,'a60ed825c1e04cff880711de63f07f86'),
 ('2021-09-05 23:37:56.781823','2021-09-05 23:37:56.781870','b99b4d09dc5b45cfb829ca4e1d17d43d','300',0,'a60ed825c1e04cff880711de63f07f86'),
 ('2021-09-05 23:38:05.279648','2021-09-05 23:38:05.279696','9d301d29d79c4aa2808b504b19b536f8','228',0,'a60ed825c1e04cff880711de63f07f86'),
 ('2021-09-05 23:38:31.556588','2021-09-05 23:38:31.556621','ad724cdf7db44a488d41a7be3e214cb8','737',1,'e52b2c0923d346e5b3d17af62f05536c'),
 ('2021-09-05 23:38:42.170741','2021-09-05 23:38:42.170785','67170dc8d8124335b90e4e4b2eb5e2b4','738',0,'e52b2c0923d346e5b3d17af62f05536c'),
 ('2021-09-05 23:38:57.182051','2021-09-05 23:38:57.182080','873478c581b34cdeafdebec4b68d6212','736',0,'e52b2c0923d346e5b3d17af62f05536c'),
 ('2021-09-05 23:39:41.306976','2021-09-05 23:39:41.307001','30f2ced33af54962b8f5902f85d2a993','789',1,'843a781d6e8849b78c2af4b77871b2a1'),
 ('2021-09-05 23:39:48.663541','2021-09-05 23:39:48.663621','442415a6cf22425d9f9448b9c027c9f0','790',0,'843a781d6e8849b78c2af4b77871b2a1'),
 ('2021-09-05 23:39:55.553340','2021-09-05 23:39:55.553364','95b95663a50548baaefbdda64a548441','787',0,'843a781d6e8849b78c2af4b77871b2a1'),
 ('2021-09-05 23:40:35.965441','2021-09-05 23:42:13.037861','7ed1c4ef40794e5e9cb0e995fee8afda','6393',1,'8019b72af5bf4d27b3b3659d3186956e'),
 ('2021-09-05 23:42:23.906815','2021-09-05 23:42:23.906844','674ef408e10546e49f4d4b47912a7f2b','6394',0,'8019b72af5bf4d27b3b3659d3186956e'),
 ('2021-09-05 23:42:31.003025','2021-09-05 23:42:31.003047','e5ebeedfd8334b2288f93d960c3ae3f1','6395',0,'8019b72af5bf4d27b3b3659d3186956e'),
 ('2021-09-05 23:42:41.892113','2021-09-05 23:42:41.892142','9423fff884d74bf7b46725613a5385eb','6347',0,'8019b72af5bf4d27b3b3659d3186956e'),
 ('2021-09-05 23:42:51.460720','2021-09-05 23:42:51.460759','7c9e6ea7997a43a2aee400ec71602bb6','6400',0,'8019b72af5bf4d27b3b3659d3186956e');
INSERT INTO "core_questionmodel" ("created_at","updated_at","id","question") VALUES ('2021-09-05 15:26:07.017665','2021-09-05 21:46:52.950577','a6b2086c021c4a03aff1fe7300fcd190','Uma confecção que produz biquínis, teve uma produção de 12 567 peças no mês de janeiro. No mês de fevereiro, como a procura foi ainda maior, foram produzidas 2 342 peças a mais que em janeiro. Quantas'),
 ('2021-09-05 15:26:19.050575','2021-09-05 15:26:19.050615','1847b6bc241e43fd8b83b2dc1f2d2e62','Uma turma tem 36 alunos e cada um deles tem um número de 1 a 36 na lista de chamada. Ontem, a professora chamou Lia ao quadro-negro e mais os outros seis alunos cujos números eram múltiplos do número'),
 ('2021-09-05 23:29:12.416411','2021-09-05 23:29:12.416436','40cb7abffd1341dc959de9e59a587dd7','Carlos deu 85 bombons para João e ficou com 415. Quantos bombons tinha Carlos?'),
 ('2021-09-05 23:29:21.060447','2021-09-05 23:29:21.060492','50baf93b8902447d98d95f3b94e87f1f','Uma caixa cabe 800 latas de sardinha, pela manhã foram colocadas 400 latas e a tarde 259. Quantas latas foram colocadas no dia todo?'),
 ('2021-09-05 23:29:28.493036','2021-09-05 23:29:28.493079','a60ed825c1e04cff880711de63f07f86','Na confeitaria tinha 400 ovos, foram comprados mais 9 dúzias e foram usados 279. Quantos ovos restaram?'),
 ('2021-09-05 23:29:35.618777','2021-09-05 23:29:35.618840','e52b2c0923d346e5b3d17af62f05536c','No restaurante foram servidos 500 almoços, 237 jantares e cada refeição foi dado uma sobremesa de cortesia. Quantas sobremesas foram dadas?'),
 ('2021-09-05 23:29:44.868383','2021-09-05 23:29:44.868425','843a781d6e8849b78c2af4b77871b2a1','Numa pasta tem 3 arquivos de documentos, o 2º arquivo tem 1.675 e o 3º arquivo tem 1.394,o total de 3.858. Quantos documentos têm no 1º arquivo?'),
 ('2021-09-05 23:29:52.553037','2021-09-05 23:29:52.553061','8019b72af5bf4d27b3b3659d3186956e','A papelaria tem 3.457 canetas azuis numa caixa, em outra caixa tem 521 a menos. Quantas canetas têm ao todo?'),
 ('2021-09-05 23:31:07.335412','2021-09-05 23:31:07.335551','a87c64a1121f4004abb1790e4522b8b6','33 * 45 ?'),
 ('2021-09-05 23:31:19.368386','2021-09-05 23:31:19.368431','208ada0e9f9742318cc0eab886e3ab9e','45 * 789?'),
 ('2021-09-05 23:31:32.110066','2021-09-05 23:31:32.110097','2ad79a31abd4402cb38eaa4a1ed00946','145 / 5?');
INSERT INTO "core_categorymodel" ("created_at","updated_at","id","name") VALUES ('2021-09-05 15:24:21.412282','2021-09-05 19:44:20.087492','de53151d804641888799626e986ab3b2','Matemática'),
 ('2021-09-05 15:29:34.605414','2021-09-05 15:29:34.605481','99cd235fe77c47d58d90fd512475d6a3','Geral'),
 ('2021-09-05 21:43:57.127851','2021-09-05 21:43:57.127887','ddfba6bacb9f43148c86f565e8cf64b0','Teste2');
INSERT INTO "core_usermodel" ("password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined","id") VALUES ('pbkdf2_sha256$260000$qjH4wDnmOcCRlbIeHZ86JZ$4gtQVnjwEg3yMBbrFeiFmiest6lDyo7zpGFfsAmi2DM=','2021-09-05 23:46:31.975432',1,'admin','Super','Administrador','admin@admin.com',1,1,'2021-09-05 15:23:39','bd7b4a43e33e4266b5ddcb874761bb1e'),
 ('pbkdf2_sha256$260000$3ybXPQbc47ADyXt6y7XP0z$oeRq8BvfeTfNwNNWogY5/foNoZyf/SRIrgIsu4YMdlY=',NULL,0,'bruno','Bruno','Martins','bruno@admin.com',0,1,'2021-09-05 15:30:47','6619b888dc2f4d8f9ce0445da5a418c3');
INSERT INTO "auth_group" ("id","name") VALUES (1,'player');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_contenttype','Can add content type'),
 (14,4,'change_contenttype','Can change content type'),
 (15,4,'delete_contenttype','Can delete content type'),
 (16,4,'view_contenttype','Can view content type'),
 (17,5,'add_session','Can add session'),
 (18,5,'change_session','Can change session'),
 (19,5,'delete_session','Can delete session'),
 (20,5,'view_session','Can view session'),
 (21,6,'add_usermodel','Can add user'),
 (22,6,'change_usermodel','Can change user'),
 (23,6,'delete_usermodel','Can delete user'),
 (24,6,'view_usermodel','Can view user'),
 (25,7,'add_categorymodel','Can add Categoria'),
 (26,7,'change_categorymodel','Can change Categoria'),
 (27,7,'delete_categorymodel','Can delete Categoria'),
 (28,7,'view_categorymodel','Can view Categoria'),
 (29,8,'add_questionmodel','Can add Pergunta'),
 (30,8,'change_questionmodel','Can change Pergunta'),
 (31,8,'delete_questionmodel','Can delete Pergunta'),
 (32,8,'view_questionmodel','Can view Pergunta'),
 (33,9,'add_answermodel','Can add Resposta'),
 (34,9,'change_answermodel','Can change Resposta'),
 (35,9,'delete_answermodel','Can delete Resposta'),
 (36,9,'view_answermodel','Can view Resposta'),
 (37,10,'add_rankingmodel','Can add Ranking'),
 (38,10,'change_rankingmodel','Can change Ranking'),
 (39,10,'delete_rankingmodel','Can delete Ranking'),
 (40,10,'view_rankingmodel','Can view Ranking'),
 (41,11,'add_categoryquestionmodel','Can add Categoria e Pergunta'),
 (42,11,'change_categoryquestionmodel','Can change Categoria e Pergunta'),
 (43,11,'delete_categoryquestionmodel','Can delete Categoria e Pergunta'),
 (44,11,'view_categoryquestionmodel','Can view Categoria e Pergunta');
INSERT INTO "auth_group_permissions" ("id","group_id","permission_id") VALUES (1,1,37),
 (2,1,38),
 (3,1,39),
 (4,1,40),
 (5,1,28);
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'contenttypes','contenttype'),
 (5,'sessions','session'),
 (6,'core','usermodel'),
 (7,'core','categorymodel'),
 (8,'core','questionmodel'),
 (9,'core','answermodel'),
 (10,'core','rankingmodel'),
 (11,'core','categoryquestionmodel');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2021-09-05 15:23:02.135482'),
 (2,'contenttypes','0002_remove_content_type_name','2021-09-05 15:23:02.156597'),
 (3,'auth','0001_initial','2021-09-05 15:23:02.181355'),
 (4,'auth','0002_alter_permission_name_max_length','2021-09-05 15:23:02.195483'),
 (5,'auth','0003_alter_user_email_max_length','2021-09-05 15:23:02.207402'),
 (6,'auth','0004_alter_user_username_opts','2021-09-05 15:23:02.217065'),
 (7,'auth','0005_alter_user_last_login_null','2021-09-05 15:23:02.227817'),
 (8,'auth','0006_require_contenttypes_0002','2021-09-05 15:23:02.232265'),
 (9,'auth','0007_alter_validators_add_error_messages','2021-09-05 15:23:02.241194'),
 (10,'auth','0008_alter_user_username_max_length','2021-09-05 15:23:02.248046'),
 (11,'auth','0009_alter_user_last_name_max_length','2021-09-05 15:23:02.253408'),
 (12,'auth','0010_alter_group_name_max_length','2021-09-05 15:23:02.261402'),
 (13,'auth','0011_update_proxy_permissions','2021-09-05 15:23:02.270360'),
 (14,'auth','0012_alter_user_first_name_max_length','2021-09-05 15:23:02.280950'),
 (15,'core','0001_initial','2021-09-05 15:23:02.314783'),
 (16,'admin','0001_initial','2021-09-05 15:23:02.334733'),
 (17,'admin','0002_logentry_remove_auto_add','2021-09-05 15:23:02.353238'),
 (18,'admin','0003_logentry_add_action_flag_choices','2021-09-05 15:23:02.369640'),
 (19,'sessions','0001_initial','2021-09-05 15:23:02.377658');
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "core_categoryquestionmodel_question_id_9f9b638c" ON "core_categoryquestionmodel" (
	"question_id"
);
CREATE INDEX IF NOT EXISTS "core_categoryquestionmodel_category_id_7898871c" ON "core_categoryquestionmodel" (
	"category_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "core_categoryquestionmodel_category_id_question_id_a4c98b0b_uniq" ON "core_categoryquestionmodel" (
	"category_id",
	"question_id"
);
CREATE INDEX IF NOT EXISTS "core_rankingmodel_user_id_c0005ce4" ON "core_rankingmodel" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "core_rankingmodel_category_id_b9017a9e" ON "core_rankingmodel" (
	"category_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "core_rankingmodel_category_id_user_id_b333a83b_uniq" ON "core_rankingmodel" (
	"category_id",
	"user_id"
);
CREATE INDEX IF NOT EXISTS "core_answermodel_question_id_339193f0" ON "core_answermodel" (
	"question_id"
);
CREATE INDEX IF NOT EXISTS "core_usermodel_user_permissions_permission_id_b05b12d7" ON "core_usermodel_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "core_usermodel_user_permissions_usermodel_id_f57a4a6b" ON "core_usermodel_user_permissions" (
	"usermodel_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "core_usermodel_user_permissions_usermodel_id_permission_id_f006c986_uniq" ON "core_usermodel_user_permissions" (
	"usermodel_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "core_usermodel_groups_group_id_3e09c396" ON "core_usermodel_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "core_usermodel_groups_usermodel_id_a8f1d790" ON "core_usermodel_groups" (
	"usermodel_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "core_usermodel_groups_usermodel_id_group_id_a1132a58_uniq" ON "core_usermodel_groups" (
	"usermodel_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
COMMIT;
