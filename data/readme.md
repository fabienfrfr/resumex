-- 1. Référentiel des consultants
CREATE TABLE consultants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    role TEXT -- Ex: 'Senior Dev', 'PM'
);

-- 2. Référentiel des compétences
CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE -- Ex: 'Python', 'AWS', 'Agile'
);

-- 3. Table de jonction (Profilage)
CREATE TABLE consultant_skills (
    consultant_id INTEGER,
    skill_id INTEGER,
    level INTEGER CHECK(level BETWEEN 1 AND 5), -- Échelle de 1 à 5
    FOREIGN KEY(consultant_id) REFERENCES consultants(id),
    FOREIGN KEY(skill_id) REFERENCES skills(id)
);

-- 4. Projets
CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    client_name TEXT,
    project_name TEXT,
    start_date DATE
);

-- 5. Staffing
CREATE TABLE staffing (
    consultant_id INTEGER,
    project_id INTEGER,
    role_on_project TEXT,
    FOREIGN KEY(consultant_id) REFERENCES consultants(id),
    FOREIGN KEY(project_id) REFERENCES projects(id)
);