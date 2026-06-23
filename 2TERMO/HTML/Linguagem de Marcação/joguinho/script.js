// =====================================
// STREET BATTLE
// SCRIPT - PARTE 1
// =====================================

// ---------- ELEMENTOS ----------

const menu = document.getElementById("menu");
const gameContainer = document.getElementById("gameContainer");
const characterSelect = document.getElementById("characterSelect");

const fighter1 = document.getElementById("fighter1");
const fighter2 = document.getElementById("fighter2");

const life1 = document.getElementById("life1");
const life2 = document.getElementById("life2");

const score1Text = document.getElementById("score1");
const score2Text = document.getElementById("score2");

const roundNumberText =
    document.getElementById("roundNumber");

const winnerScreen =
    document.getElementById("winnerScreen");

const winnerText =
    document.getElementById("winnerText");

// ---------- CONFIG ----------

const ARENA_WIDTH = 1200;
const GROUND = 120;

// ---------- PERSONAGENS ----------

const characters = {

    Ninja: {
        speed: 8,
        damage: 8,
        specialDamage: 15,
        color: "ninja"
    },

    Samurai: {
        speed: 5,
        damage: 13,
        specialDamage: 20,
        color: "samurai"
    },

    Monge: {
        speed: 6,
        damage: 10,
        specialDamage: 18,
        color: "monge"
    },

    Robô: {
        speed: 4,
        damage: 16,
        specialDamage: 24,
        color: "robo"
    },

    Dragão: {
        speed: 7,
        damage: 12,
        specialDamage: 22,
        color: "dragao"
    }

};

// ---------- ESTADO ----------

let gameMode = null;

let selectedPlayer1 = null;
let selectedPlayer2 = null;

let selectionStep = 1;

let round = 1;

let score1 = 0;
let score2 = 0;

// ---------- LUTADORES ----------

const player1 = {

    x: 150,
    y: 0,

    width: 90,
    height: 150,

    life: 100,

    speed: 6,

    damage: 10,

    specialDamage: 20,

    jumping: false

};

const player2 = {

    x: 900,
    y: 0,

    width: 90,
    height: 150,

    life: 100,

    speed: 6,

    damage: 10,

    specialDamage: 20,

    jumping: false

};

// ---------- TECLAS ----------

const keys = {};

// =====================================
// MODO DE JOGO
// =====================================

function selectMode(mode) {

    gameMode = mode;

    characterSelect.classList.remove("hidden");

}

// =====================================
// ESCOLHA DE PERSONAGEM
// =====================================

function chooseCharacter(name) {

    if (selectionStep === 1) {

        selectedPlayer1 = name;

        document.getElementById(
            "selectionInfo"
        ).innerHTML =

            `
        <p>Jogador 1:
        ${selectedPlayer1}</p>

        <p>Jogador 2:
        Não selecionado</p>
        `;

        selectionStep = 2;

        return;
    }

    selectedPlayer2 = name;

    document.getElementById(
        "selectionInfo"
    ).innerHTML =

        `
    <p>Jogador 1:
    ${selectedPlayer1}</p>

    <p>Jogador 2:
    ${selectedPlayer2}</p>
    `;

    setTimeout(startGame, 1000);

}

// =====================================
// INICIAR PARTIDA
// =====================================

function startGame() {

    menu.classList.add("hidden");

    gameContainer.classList.remove("hidden");

    applyCharacter(player1,
        selectedPlayer1,
        fighter1);

    applyCharacter(player2,
        selectedPlayer2,
        fighter2);

    resetRound();

}

// =====================================
// APLICAR PERSONAGEM
// =====================================

function applyCharacter(
    player,
    characterName,
    element
) {

    const data =
        characters[characterName];

    player.speed =
        data.speed;

    player.damage =
        data.damage;

    player.specialDamage =
        data.specialDamage;

    element.classList.add(
        data.color
    );

}

// =====================================
// RESET ROUND
// =====================================

function resetRound() {

    player1.life = 100;
    player2.life = 100;

    player1.x = 150;
    player2.x = 900;

    updateLifeBars();

    updatePositions();

}

// =====================================
// VIDA
// =====================================

function updateLifeBars() {

    life1.style.width =
        player1.life + "%";

    life2.style.width =
        player2.life + "%";

    if (player1.life > 60)
        life1.style.background =
            "limegreen";

    else if (player1.life > 30)
        life1.style.background =
            "orange";

    else
        life1.style.background =
            "red";

    if (player2.life > 60)
        life2.style.background =
            "limegreen";

    else if (player2.life > 30)
        life2.style.background =
            "orange";

    else
        life2.style.background =
            "red";

}

// =====================================
// POSIÇÃO
// =====================================

function updatePositions() {

    fighter1.style.left =
        player1.x + "px";

    fighter2.style.left =
        player2.x + "px";

}

// =====================================
// MOVIMENTO
// =====================================

function movePlayers() {

    // PLAYER 1

    if (keys["a"]) {

        player1.x -=
            player1.speed;

        fighter1.classList.add(
            "walk"
        );
    }

    if (keys["d"]) {

        player1.x +=
            player1.speed;

        fighter1.classList.add(
            "walk"
        );
    }

    // PLAYER 2

    if (gameMode === "pvp") {

        if (keys["ArrowLeft"]) {

            player2.x -=
                player2.speed;

            fighter2.classList.add(
                "walk"
            );
        }

        if (keys["ArrowRight"]) {

            player2.x +=
                player2.speed;

            fighter2.classList.add(
                "walk"
            );
        }

    }

    // LIMITES

    player1.x =
        Math.max(
            0,
            Math.min(
                ARENA_WIDTH -
                player1.width,
                player1.x
            ));

    player2.x =
        Math.max(
            0,
            Math.min(
                ARENA_WIDTH -
                player2.width,
                player2.x
            ));

    updatePositions();

}

// =====================================
// PULO
// =====================================

function jump(player, element) {

    if (player.jumping)
        return;

    player.jumping = true;

    element.classList.add(
        "jump"
    );

    setTimeout(() => {

        element.classList.remove(
            "jump"
        );

        player.jumping = false;

    }, 600);

}

// =====================================
// CONTROLES
// =====================================

window.addEventListener(
    "keydown",
    (e) => {

        keys[e.key] = true;

        if (e.key === "w") {

            jump(player1, fighter1);

        }

        if (
            gameMode === "pvp" &&
            e.key === "ArrowUp"
        ) {

            jump(player2, fighter2);

        }

    });

window.addEventListener(
    "keyup",
    (e) => {

        keys[e.key] = false;

        fighter1.classList.remove(
            "walk"
        );

        fighter2.classList.remove(
            "walk"
        );

    });

// =====================================
// ROUND
// =====================================

function updateScore() {

    score1Text.innerText =
        "Rounds: " + score1;

    score2Text.innerText =
        "Rounds: " + score2;

    roundNumberText.innerText =
        round;

}

// =====================================
// GAME LOOP
// =====================================

function gameLoop() {

    movePlayers();

    requestAnimationFrame(
        gameLoop
    );

}

gameLoop();

// =====================================
// COMBATE
// PARTE 2
// =====================================

// ---------- COLISÃO ----------

function isColliding() {

    return (

        player1.x <
        player2.x + player2.width &&

        player1.x + player1.width >
        player2.x

    );

}

// ---------- DANO ----------

function dealDamage(target, amount) {

    target.life -= amount;

    if (target.life < 0)
        target.life = 0;

    updateLifeBars();

    checkRoundWinner();

}

// ---------- KNOCKBACK ----------

function knockbackPlayer1() {

    player1.x -= 40;

    if (player1.x < 0)
        player1.x = 0;

}

function knockbackPlayer2() {

    player2.x += 40;

    if (player2.x > 1110)
        player2.x = 1110;

}

// ---------- ATAQUE NORMAL ----------

function attackPlayer1() {

    fighter1.classList.add("attack");

    setTimeout(() => {

        fighter1.classList.remove(
            "attack"
        );

    }, 150);

    if (isColliding()) {

        fighter2.classList.add("hit");

        setTimeout(() => {

            fighter2.classList.remove(
                "hit"
            );

        }, 200);

        dealDamage(
            player2,
            player1.damage
        );

        knockbackPlayer2();

    }

}

function attackPlayer2() {

    fighter2.classList.add("attack");

    setTimeout(() => {

        fighter2.classList.remove(
            "attack"
        );

    }, 150);

    if (isColliding()) {

        fighter1.classList.add("hit");

        setTimeout(() => {

            fighter1.classList.remove(
                "hit"
            );

        }, 200);

        dealDamage(
            player1,
            player2.damage
        );

        knockbackPlayer1();

    }

}

// ---------- PROJÉTIL ----------

function createProjectile(
    owner,
    target,
    damage
) {
    function getProjectileColor(character) {

        switch (character) {

            case "Ninja":
                return "white";

            case "Samurai":
                return "red";

            case "Monge":
                return "cyan";

            case "Robô":
                return "magenta";

            case "Dragão":
                return "orange";

            default:
                return "yellow";
        }

        let characterName =
            owner === player1
                ? selectedPlayer1
                : selectedPlayer2;

        projectile.style.background =
            getProjectileColor(characterName);

        projectile.style.boxShadow =
            `0 0 20px ${getProjectileColor(characterName)}`;
    }
    const projectile =
        document.createElement("div");

    projectile.classList.add(
        "projectile"
    );
    let characterName =
        owner === player1
            ? selectedPlayer1
            : selectedPlayer2;

    projectile.style.background =
        getProjectileColor(characterName);

    projectile.style.boxShadow =
        `0 0 20px ${getProjectileColor(characterName)}`;
    document
        .getElementById("arena")
        .appendChild(projectile);

    let posX =
        owner.x + 40;

    projectile.style.left =
        posX + "px";

    projectile.style.bottom =
        "220px";

    const direction =
        owner === player1
            ? 1
            : -1;

    const move = setInterval(() => {

        posX +=
            10 * direction;

        projectile.style.left =
            posX + "px";

        const hit =

            direction === 1

                ? posX >= target.x

                : posX <=
                target.x + 40;

        if (hit) {

            clearInterval(move);

            projectile.remove();

            if (target === player1) {

                fighter1.classList.add(
                    "hit"
                );

                setTimeout(() => {

                    fighter1.classList.remove(
                        "hit"
                    );

                }, 200);

            } else {

                fighter2.classList.add(
                    "hit"
                );

                setTimeout(() => {

                    fighter2.classList.remove(
                        "hit"
                    );

                }, 200);

            }

            dealDamage(
                target,
                damage
            );

        }

        if (
            posX < -50 ||
            posX > 1400
        ) {

            clearInterval(move);

            projectile.remove();

        }

    }, 16);

}

// ---------- ESPECIAL ----------

function specialPlayer1() {

    createProjectile(
        player1,
        player2,
        player1.specialDamage
    );

}

function specialPlayer2() {

    createProjectile(
        player2,
        player1,
        player2.specialDamage
    );

}

// ---------- VENCEDOR DO ROUND ----------

function checkRoundWinner() {

    if (player1.life <= 0) {

        score2++;

        updateScore();

        setTimeout(() => {

            nextRound();

        }, 1200);

    }

    if (player2.life <= 0) {

        score1++;

        updateScore();

        setTimeout(() => {

            nextRound();

        }, 1200);

    }

}

// ---------- PRÓXIMO ROUND ----------

function nextRound() {

    if (score1 >= 3) {

        showWinner(
            "Jogador 1"
        );

        return;
    }

    if (score2 >= 3) {

        if (gameMode === "bot") {

            showWinner(
                "BOT"
            );

        } else {

            showWinner(
                "Jogador 2"
            );

        }

        return;
    }

    round++;

    updateScore();

    resetRound();

}

// ---------- VENCEDOR FINAL ----------

function showWinner(name) {

    gameContainer.classList.add(
        "hidden"
    );

    winnerScreen.classList.remove(
        "hidden"
    );

    winnerText.innerText =
        name + " venceu!";

}

// =====================================
// CONTROLES DE COMBATE
// =====================================

window.addEventListener(
    "keydown",
    (e) => {

        // PLAYER 1

        if (e.key === "f") {

            attackPlayer1();

        }

        if (e.key === "g") {

            specialPlayer1();

        }

        // PLAYER 2

        if (gameMode === "pvp") {

            if (e.key === "k") {

                attackPlayer2();

            }

            if (e.key === "l") {

                specialPlayer2();

            }

        }

    });

// =====================================
// STREET BATTLE
// SCRIPT - PARTE FINAL
// =====================================

// ----------------------
// COOLDOWNS
// ----------------------

let p1AttackCooldown = false;
let p2AttackCooldown = false;

let p1SpecialCooldown = false;
let p2SpecialCooldown = false;

// ----------------------
// MENSAGEM NA TELA
// ----------------------

function showMessage(text) {

    const msg =
        document.createElement("div");

    msg.className =
        "roundMessage";

    msg.innerText = text;

    document
        .getElementById("arena")
        .appendChild(msg);

    setTimeout(() => {

        msg.remove();

    }, 1500);

}

// ----------------------
// ROUND VISUAL
// ----------------------

const originalResetRound =
    resetRound;

resetRound = function () {

    player1.life = 100;
    player2.life = 100;

    player1.x = 150;
    player2.x = 900;

    updateLifeBars();
    updatePositions();

    showMessage(
        "ROUND " + round
    );

    setTimeout(() => {

        showMessage("FIGHT!");

    }, 1000);

};

// ----------------------
// ATAQUES COM COOLDOWN
// ----------------------

const originalAttackP1 =
    attackPlayer1;

attackPlayer1 = function () {

    if (p1AttackCooldown)
        return;

    p1AttackCooldown = true;

    originalAttackP1();

    setTimeout(() => {

        p1AttackCooldown = false;

    }, 500);

};

const originalAttackP2 =
    attackPlayer2;

attackPlayer2 = function () {

    if (p2AttackCooldown)
        return;

    p2AttackCooldown = true;

    originalAttackP2();

    setTimeout(() => {

        p2AttackCooldown = false;

    }, 500);

};

// ----------------------
// ESPECIAL COM COOLDOWN
// ----------------------

const originalSpecialP1 =
    specialPlayer1;

specialPlayer1 = function () {

    if (p1SpecialCooldown)
        return;

    p1SpecialCooldown = true;

    originalSpecialP1();

    setTimeout(() => {

        p1SpecialCooldown = false;

    }, 2500);

};

const originalSpecialP2 =
    specialPlayer2;

specialPlayer2 = function () {

    if (p2SpecialCooldown)
        return;

    p2SpecialCooldown = true;

    originalSpecialP2();

    setTimeout(() => {

        p2SpecialCooldown = false;

    }, 2500);

};

// ----------------------
// IA DO BOT
// ----------------------

function botLogic() {

    if (gameMode !== "bot")
        return;

    const distance =
        Math.abs(
            player1.x -
            player2.x
        );

    // aproximar

    if (distance > 110) {

        if (player2.x > player1.x) {

            player2.x -=
                player2.speed;

        } else {

            player2.x +=
                player2.speed;

        }

    }

    // soco

    if (distance < 110) {

        if (
            Math.random() <
            0.03
        ) {

            attackPlayer2();

        }

    }

    // especial

    if (
        distance > 180 &&
        Math.random() < 0.006
    ) {

        specialPlayer2();

    }

}

// ----------------------
// MELHORIAS VISUAIS
// ----------------------

function faceOpponent() {

    if (player1.x < player2.x) {

        fighter1.style.transform =
            "scaleX(1)";

        fighter2.style.transform =
            "scaleX(-1)";

    } else {

        fighter1.style.transform =
            "scaleX(-1)";

        fighter2.style.transform =
            "scaleX(1)";

    }

}

// ----------------------
// SOMBRA DE VIDA
// ----------------------

function updateLifeEffects() {

    if (player1.life < 30) {

        fighter1.style.boxShadow =
            "0 0 20px red";

    } else {

        fighter1.style.boxShadow =
            "none";

    }

    if (player2.life < 30) {

        fighter2.style.boxShadow =
            "0 0 20px red";

    } else {

        fighter2.style.boxShadow =
            "none";

    }

}

// ----------------------
// MELHORIA DO LOOP
// ----------------------

const oldGameLoop =
    gameLoop;

function enhancedLoop() {

    movePlayers();

    botLogic();

    faceOpponent();

    updateLifeEffects();

    updatePositions();

    requestAnimationFrame(
        enhancedLoop
    );

}

// interrompe loop antigo

window.cancelAnimationFrame =
    window.cancelAnimationFrame || function () { };

// inicia loop novo

enhancedLoop();

// ----------------------
// NOME DOS PERSONAGENS
// ----------------------

const oldStartGame =
    startGame;

startGame = function () {

    oldStartGame();

    document
        .getElementById("p1Name")
        .innerText =
        selectedPlayer1;

    document
        .getElementById("p2Name")
        .innerText =

        gameMode === "bot"
            ? "BOT - " +
            selectedPlayer2
            : selectedPlayer2;
    document.getElementById("p1Commands").innerHTML =
        `
F = Ataque |
G = ${characters[selectedPlayer1].special}
`;

    document.getElementById("p2Commands").innerHTML =
        `
K = Ataque |
L = ${characters[selectedPlayer2].special}
`;
};

// ----------------------
// INFORMAÇÃO INICIAL
// ----------------------

console.log(
    "Street Battle carregado!"
);

function updateCommands() {

    document.getElementById("p1Commands").innerHTML =
        `F = Ataque | G = ${characters[selectedPlayer1].special}`;

    if (gameMode === "bot") {

        document.getElementById("p2Commands").innerHTML =
            `BOT`;

    } else {

        document.getElementById("p2Commands").innerHTML =
            `K = Ataque | L = ${characters[selectedPlayer2].special}`;

    }

}