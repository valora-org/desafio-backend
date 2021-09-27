--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.3 (Debian 13.3-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO postgres;

--
-- Name: core_categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.core_categoria (
    id bigint NOT NULL,
    categoria_texto character varying(200) NOT NULL
);


ALTER TABLE public.core_categoria OWNER TO postgres;

--
-- Name: core_categoria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.core_categoria_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_categoria_id_seq OWNER TO postgres;

--
-- Name: core_categoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.core_categoria_id_seq OWNED BY public.core_categoria.id;


--
-- Name: core_pergunta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.core_pergunta (
    id bigint NOT NULL,
    pergunta_texto character varying(200) NOT NULL,
    categoria_id bigint NOT NULL
);


ALTER TABLE public.core_pergunta OWNER TO postgres;

--
-- Name: core_pergunta_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.core_pergunta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_pergunta_id_seq OWNER TO postgres;

--
-- Name: core_pergunta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.core_pergunta_id_seq OWNED BY public.core_pergunta.id;


--
-- Name: core_quiz; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.core_quiz (
    id bigint NOT NULL,
    pontos integer NOT NULL,
    usuario_id bigint NOT NULL,
    questao_respondida integer NOT NULL
);


ALTER TABLE public.core_quiz OWNER TO postgres;

--
-- Name: core_quiz_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.core_quiz_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_quiz_id_seq OWNER TO postgres;

--
-- Name: core_quiz_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.core_quiz_id_seq OWNED BY public.core_quiz.id;


--
-- Name: core_quiz_perguntas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.core_quiz_perguntas (
    id bigint NOT NULL,
    quiz_id bigint NOT NULL,
    pergunta_id bigint NOT NULL
);


ALTER TABLE public.core_quiz_perguntas OWNER TO postgres;

--
-- Name: core_quiz_perguntas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.core_quiz_perguntas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_quiz_perguntas_id_seq OWNER TO postgres;

--
-- Name: core_quiz_perguntas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.core_quiz_perguntas_id_seq OWNED BY public.core_quiz_perguntas.id;


--
-- Name: core_resposta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.core_resposta (
    id bigint NOT NULL,
    resposta_texto character varying(200) NOT NULL,
    correta boolean NOT NULL,
    pergunta_id bigint NOT NULL
);


ALTER TABLE public.core_resposta OWNER TO postgres;

--
-- Name: core_resposta_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.core_resposta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_resposta_id_seq OWNER TO postgres;

--
-- Name: core_resposta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.core_resposta_id_seq OWNED BY public.core_resposta.id;


--
-- Name: core_usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.core_usuario (
    id bigint NOT NULL,
    admin boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.core_usuario OWNER TO postgres;

--
-- Name: core_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.core_usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_usuario_id_seq OWNER TO postgres;

--
-- Name: core_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.core_usuario_id_seq OWNED BY public.core_usuario.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: core_categoria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_categoria ALTER COLUMN id SET DEFAULT nextval('public.core_categoria_id_seq'::regclass);


--
-- Name: core_pergunta id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_pergunta ALTER COLUMN id SET DEFAULT nextval('public.core_pergunta_id_seq'::regclass);


--
-- Name: core_quiz id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz ALTER COLUMN id SET DEFAULT nextval('public.core_quiz_id_seq'::regclass);


--
-- Name: core_quiz_perguntas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz_perguntas ALTER COLUMN id SET DEFAULT nextval('public.core_quiz_perguntas_id_seq'::regclass);


--
-- Name: core_resposta id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_resposta ALTER COLUMN id SET DEFAULT nextval('public.core_resposta_id_seq'::regclass);


--
-- Name: core_usuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_usuario ALTER COLUMN id SET DEFAULT nextval('public.core_usuario_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add categoria	7	add_categoria
26	Can change categoria	7	change_categoria
27	Can delete categoria	7	delete_categoria
28	Can view categoria	7	view_categoria
29	Can add pergunta	8	add_pergunta
30	Can change pergunta	8	change_pergunta
31	Can delete pergunta	8	delete_pergunta
32	Can view pergunta	8	view_pergunta
33	Can add usuario	9	add_usuario
34	Can change usuario	9	change_usuario
35	Can delete usuario	9	delete_usuario
36	Can view usuario	9	view_usuario
37	Can add resposta	10	add_resposta
38	Can change resposta	10	change_resposta
39	Can delete resposta	10	delete_resposta
40	Can view resposta	10	view_resposta
41	Can add quiz	11	add_quiz
42	Can change quiz	11	change_quiz
43	Can delete quiz	11	delete_quiz
44	Can view quiz	11	view_quiz
45	Can add Token	12	add_token
46	Can change Token	12	change_token
47	Can delete Token	12	delete_token
48	Can view Token	12	view_token
49	Can add token	13	add_tokenproxy
50	Can change token	13	change_tokenproxy
51	Can delete token	13	delete_tokenproxy
52	Can view token	13	view_tokenproxy
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$260000$CVXtkicxd4mUThI2DjqDuR$eqIo/TenbrDP2MpW8C8wtMvlJcxZSIXKuvBhkIbfOIM=	\N	f	alice	Alice			f	t	2021-09-23 05:21:15+00
2	pbkdf2_sha256$260000$Xzsw0qfPqcsRLity3WNvzF$gKbyVCEqUedTF5spGcq9VHiKOm4UFm2peAosL8im9Zc=	\N	f	raphael	Raphael	Oliveira		f	t	2021-09-21 15:00:49+00
1	pbkdf2_sha256$260000$ScAnqvanjmG8bWTrC2HJOU$EryOJHJLEd984yk84wgY74FraAg2BF11ct+olqcYAVc=	2021-09-24 22:57:54.029531+00	t	root				t	t	2021-09-20 15:34:29.185926+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
504734f4f2d15068240839b56128aea0fe6ec0e5	2021-09-25 18:32:19.31715+00	3
5604dc8b53e36d11229587968c44df882222e2e4	2021-09-25 18:32:23.820383+00	2
\.


--
-- Data for Name: core_categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_categoria (id, categoria_texto) FROM stdin;
1	esporte
\.


--
-- Data for Name: core_pergunta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_pergunta (id, pergunta_texto, categoria_id) FROM stdin;
1	Quem foi o campeão da copa do mundo de 1994?	1
2	Quem é conhecido como o rei do futebol?	1
3	Qual é o nome da primeira liga de futebol alemã?	1
7	Em que time espanhol Andrés Iniesta jogou?	1
10	Quantas equipes jogam na Primeira Divisão da liga espanhola?	1
12	Qual time foi o campeão da copa do mundial de futebol de 2014?	1
13	Em que país pertence a Liga Calcio?	1
14	Quando Lionel Messi ganhou sua primeira bola de ouro?	1
15	Quantas copas do mundo Cafu ganhou?	1
16	Em que ano foi fundado o FC Barcelona?	1
17	Em que clube Ronaldo Nazário estreou?	1
21	Qual jogador mais novo a ganhar uma copa do mundo?	1
\.


--
-- Data for Name: core_quiz; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_quiz (id, pontos, usuario_id, questao_respondida) FROM stdin;
\.


--
-- Data for Name: core_quiz_perguntas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_quiz_perguntas (id, quiz_id, pergunta_id) FROM stdin;
\.


--
-- Data for Name: core_resposta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_resposta (id, resposta_texto, correta, pergunta_id) FROM stdin;
1	Brasil	t	1
2	Argentina	f	1
3	Itália	f	1
4	Pelé	t	2
5	Maradona	f	2
6	Messi	f	2
7	Bundesliga	t	3
8	La Liga	f	3
9	Libertadores	f	3
19	Barcelona	t	7
20	Real Madri	f	7
21	Servilla	f	7
28	20	t	10
29	16	f	10
30	18	f	10
35	Alemanha	t	12
36	Bélgica	f	12
37	Itália	f	12
38	Itália	t	13
39	Espanha	f	13
40	Alemanha	f	13
41	2009	t	14
42	2010	f	14
43	2011	f	14
44	2	t	15
45	1	f	15
46	3	f	15
47	1899	t	16
48	1851	f	16
49	1799	f	16
50	Cruzeiro	t	17
51	Corinthians	f	17
52	Grêmio	f	17
57	Pelé	t	21
58	Mbappé	f	21
59	Ronaldo	f	21
\.


--
-- Data for Name: core_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_usuario (id, admin, user_id) FROM stdin;
1	f	2
2	t	3
\.

--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	core	categoria
8	core	pergunta
9	core	usuario
10	core	resposta
11	core	quiz
12	authtoken	token
13	authtoken	tokenproxy
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-09-20 15:34:09.783615+00
2	auth	0001_initial	2021-09-20 15:34:11.127917+00
3	admin	0001_initial	2021-09-20 15:34:11.45132+00
4	admin	0002_logentry_remove_auto_add	2021-09-20 15:34:11.51614+00
5	admin	0003_logentry_add_action_flag_choices	2021-09-20 15:34:11.567643+00
6	contenttypes	0002_remove_content_type_name	2021-09-20 15:34:11.623818+00
7	auth	0002_alter_permission_name_max_length	2021-09-20 15:34:11.667965+00
8	auth	0003_alter_user_email_max_length	2021-09-20 15:34:11.70371+00
9	auth	0004_alter_user_username_opts	2021-09-20 15:34:11.768832+00
10	auth	0005_alter_user_last_login_null	2021-09-20 15:34:11.818533+00
11	auth	0006_require_contenttypes_0002	2021-09-20 15:34:11.848175+00
12	auth	0007_alter_validators_add_error_messages	2021-09-20 15:34:11.882107+00
13	auth	0008_alter_user_username_max_length	2021-09-20 15:34:11.971624+00
14	auth	0009_alter_user_last_name_max_length	2021-09-20 15:34:12.041372+00
15	auth	0010_alter_group_name_max_length	2021-09-20 15:34:12.090467+00
16	auth	0011_update_proxy_permissions	2021-09-20 15:34:12.130727+00
17	auth	0012_alter_user_first_name_max_length	2021-09-20 15:34:12.167736+00
18	core	0001_initial	2021-09-20 15:34:13.140827+00
19	sessions	0001_initial	2021-09-20 15:34:13.446247+00
20	core	0002_quiz_questao_respondida	2021-09-22 22:15:08.356169+00
21	core	0003_auto_20210923_0259	2021-09-23 05:59:17.242339+00
22	authtoken	0001_initial	2021-09-25 18:31:11.762105+00
23	authtoken	0002_auto_20160226_1747	2021-09-25 18:31:11.867183+00
24	authtoken	0003_tokenproxy	2021-09-25 18:31:11.89963+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
2idoo9slarbc5p0qwchxr7o45eqhhyc3	.eJxVjMEOwiAQRP-FsyFQoIBH734D2V22UjU0Ke3J-O9K0oMmc5r3Zl4iwb6VtDde05zFWWhx-u0Q6MG1g3yHelskLXVbZ5RdkQdt8rpkfl4O9--gQCt9nUfHmjUGr8AAGUfAkzfOO2uUjhCGySOS_YbYRJ0D0-gjkkJrwiDeH_nJOFs:1mTQs6:5iqDvRM5phs01Po7fFcJn4HRN1x7Xp2yfbJm6D6YyiE	2021-10-07 15:42:50.026535+00
bt88pxq1lknd7h7gor898wmcu0ee7zcv	.eJxVjMEOwiAQRP-FsyFQoIBH734D2V22UjU0Ke3J-O9K0oMmc5r3Zl4iwb6VtDde05zFWWhx-u0Q6MG1g3yHelskLXVbZ5RdkQdt8rpkfl4O9--gQCt9nUfHmjUGr8AAGUfAkzfOO2uUjhCGySOS_YbYRJ0D0-gjkkJrwiDeH_nJOFs:1mTu8g:Dv5vwAbnePoQJsP8Fxxn4RUAcBKcWX524oNWdmwFOPE	2021-10-08 22:57:54.079382+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 5, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: core_categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_categoria_id_seq', 1, true);


--
-- Name: core_pergunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_pergunta_id_seq', 22, true);


--
-- Name: core_quiz_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_quiz_id_seq', 45, true);


--
-- Name: core_quiz_perguntas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_quiz_perguntas_id_seq', 253, true);


--
-- Name: core_resposta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_resposta_id_seq', 62, true);


--
-- Name: core_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_usuario_id_seq', 3, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 142, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: core_categoria core_categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_categoria
    ADD CONSTRAINT core_categoria_pkey PRIMARY KEY (id);


--
-- Name: core_pergunta core_pergunta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_pergunta
    ADD CONSTRAINT core_pergunta_pkey PRIMARY KEY (id);


--
-- Name: core_quiz_perguntas core_quiz_perguntas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz_perguntas
    ADD CONSTRAINT core_quiz_perguntas_pkey PRIMARY KEY (id);


--
-- Name: core_quiz_perguntas core_quiz_perguntas_quiz_id_pergunta_id_63495443_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz_perguntas
    ADD CONSTRAINT core_quiz_perguntas_quiz_id_pergunta_id_63495443_uniq UNIQUE (quiz_id, pergunta_id);


--
-- Name: core_quiz core_quiz_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz
    ADD CONSTRAINT core_quiz_pkey PRIMARY KEY (id);


--
-- Name: core_resposta core_resposta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_resposta
    ADD CONSTRAINT core_resposta_pkey PRIMARY KEY (id);


--
-- Name: core_usuario core_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_usuario
    ADD CONSTRAINT core_usuario_pkey PRIMARY KEY (id);


--
-- Name: core_usuario core_usuario_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_usuario
    ADD CONSTRAINT core_usuario_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: core_pergunta_categoria_id_9898dff7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX core_pergunta_categoria_id_9898dff7 ON public.core_pergunta USING btree (categoria_id);


--
-- Name: core_quiz_perguntas_pergunta_id_6a8aa431; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX core_quiz_perguntas_pergunta_id_6a8aa431 ON public.core_quiz_perguntas USING btree (pergunta_id);


--
-- Name: core_quiz_perguntas_quiz_id_346c57a8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX core_quiz_perguntas_quiz_id_346c57a8 ON public.core_quiz_perguntas USING btree (quiz_id);


--
-- Name: core_quiz_usuario_id_b5e5e905; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX core_quiz_usuario_id_b5e5e905 ON public.core_quiz USING btree (usuario_id);


--
-- Name: core_resposta_pergunta_id_1316eebb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX core_resposta_pergunta_id_1316eebb ON public.core_resposta USING btree (pergunta_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_pergunta core_pergunta_categoria_id_9898dff7_fk_core_categoria_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_pergunta
    ADD CONSTRAINT core_pergunta_categoria_id_9898dff7_fk_core_categoria_id FOREIGN KEY (categoria_id) REFERENCES public.core_categoria(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_quiz_perguntas core_quiz_perguntas_pergunta_id_6a8aa431_fk_core_pergunta_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz_perguntas
    ADD CONSTRAINT core_quiz_perguntas_pergunta_id_6a8aa431_fk_core_pergunta_id FOREIGN KEY (pergunta_id) REFERENCES public.core_pergunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_quiz_perguntas core_quiz_perguntas_quiz_id_346c57a8_fk_core_quiz_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz_perguntas
    ADD CONSTRAINT core_quiz_perguntas_quiz_id_346c57a8_fk_core_quiz_id FOREIGN KEY (quiz_id) REFERENCES public.core_quiz(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_quiz core_quiz_usuario_id_b5e5e905_fk_core_usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_quiz
    ADD CONSTRAINT core_quiz_usuario_id_b5e5e905_fk_core_usuario_id FOREIGN KEY (usuario_id) REFERENCES public.core_usuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_resposta core_resposta_pergunta_id_1316eebb_fk_core_pergunta_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_resposta
    ADD CONSTRAINT core_resposta_pergunta_id_1316eebb_fk_core_pergunta_id FOREIGN KEY (pergunta_id) REFERENCES public.core_pergunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_usuario core_usuario_user_id_19419638_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.core_usuario
    ADD CONSTRAINT core_usuario_user_id_19419638_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

