<img src="./assets/banner.svg" width="100%" alt="John Mokaya - Nairobi, livestock telemetry written on-chain" />

```
mokayaj857@nairobi
------------------
os:       full-stack / web3
host:     HerdSecure
kernel:   typescript + solidity
packages: eth avax dot ada sui
shell:    foundry  |  hardhat  |  next
wm:       nairobi, ke
uptime:   compiling since the first collar
cpu:      curiosity
gpu:      zk proofs (warming up)
```

<p align="center">
  <a href="https://readme-typing-svg.demolab.com">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2800&pause=700&color=7DD3A0&center=true&vCenter=true&width=900&height=40&lines=%24+tail+-f+%2Fvar%2Flog%2Fherdsecure.log;collar+ping+ok+%7C+rssi%3D-91+%7C+proof%3Don-chain;Ethereum+%C2%B7+Avalanche+%C2%B7+Polkadot+%C2%B7+Cardano+%C2%B7+Sui;from+Nairobi+with+a+LoRa+radio+and+a+keystore" alt="boot ticker" />
  </a>
</p>

<p align="center">
  <a href="mailto:mokayaj857@gmail.com"><img src="https://img.shields.io/badge/smtp-mokayaj857%40gmail.com-0b0a09?style=for-the-badge&logo=gmail&logoColor=e85d04&labelColor=16110e" alt="email" /></a>
  <a href="https://linkedin.com/in/john-mokaya-3b926a261"><img src="https://img.shields.io/badge/ldap-john.mokaya-0b0a09?style=for-the-badge&logo=linkedin&logoColor=c4a574&labelColor=16110e" alt="linkedin" /></a>
  <a href="https://john-mokaya.vercel.app/"><img src="https://img.shields.io/badge/origin-john--mokaya.vercel.app-0b0a09?style=for-the-badge&logo=vercel&logoColor=f4efe6&labelColor=16110e" alt="portfolio" /></a>
  <a href="https://github.com/mokayaj857"><img src="https://img.shields.io/badge/git-mokayaj857-0b0a09?style=for-the-badge&logo=github&logoColor=7dd3a0&labelColor=16110e" alt="github" /></a>
  <img src="https://komarev.com/ghpvc/?username=mokayaj857&color=e85d04&style=for-the-badge&label=log+reads&labelColor=16110e" alt="views" />
</p>

<img src="./assets/boot.svg" width="100%" alt="herdsecure gateway journalctl dump" />

---

### `man john`

A stolen cow is usually gossip. Gossip does not survive a hash.

I design full-stack systems with a Web3 core, then I actually ship them. The flagship is **[HerdSecure](https://john-mokaya.vercel.app/)**: collars on livestock, LoRa in the bush, an indexer that is picky about signatures, and an attestation that lands on a ledger. If the animal moves, the chain is supposed to know. If it does not, that is a bug, not a vibe.

Nairobi is the lab. The stack is whatever gets a packet from a neck to a block without lying.

<img src="./assets/proc.svg" width="100%" alt="/proc/self/status for john" />

<img src="./assets/frame.svg" width="100%" alt="captured LoRa frame hex dump" />

---

### packet path

```
  [ collar / GPS / IMU ]
           |  LoRaWAN  sf9  125kHz
           v
     [ gateway nbo-gw-01 ]
           |  MQTT  herd/ke/+/+
           v
     [ indexer + signer ]
           |  keccak(tag || latE7 || lngE7 || ts)
           v
   +-------+--------+---------+--------+
   |  EVM  |  DOT   |  eUTxO  |  Move  |
   |  AVAX |  XCM   |  Aiken  |  Sui   |
   +-------+--------+---------+--------+
           |
           v
     [ watchtower ]
       geofence · heartbeat · alert
```

```mermaid
sequenceDiagram
    autonumber
    participant C as Collar 0x857
    participant G as Gateway
    participant I as Indexer
    participant L as Ledger
    participant W as Watchtower
    C->>G: LoRa ping (gps, rssi, nonce)
    G->>I: MQTT herd/ke/nbo/0x857
    I->>I: verify sig + replay window
    I->>L: attest(tag, geo, ts)
    L-->>I: tx hash / extrinsic / object id
    I->>W: proof receipt
    W-->>C: heartbeat ok (or siren)
```

---

### `$ cat contracts/HeadCount.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface IHerd {
    event HeadCount(
        bytes32 indexed herd,
        uint256 indexed tag,
        int32 latE7,
        int32 lngE7,
        uint64 ts
    );

    function attest(
        bytes32 herd,
        uint256 tag,
        int32 latE7,
        int32 lngE7,
        uint64 ts,
        bytes calldata sig
    ) external;
}
```

```move
module herd::secure {
    struct Collar has key { tag: u64, lat_e7: i32, lng_e7: i32, ts: u64 }
    public fun ping(c: &mut Collar, lat: i32, lng: i32, ts: u64) {
        c.lat_e7 = lat; c.lng_e7 = lng; c.ts = ts;
    }
}
```

```aiken
pub type Datum { HeadCount { tag: ByteArray, geo: ByteArray, epoch: Int } }
```

<img src="./assets/constellation.svg" width="100%" alt="signal map origin Nairobi" />

<details>
<summary><b>chain notes (click)</b> — the stuff behind the logos</summary>

**Ethereum / EVM** — Solidity, ERC-20 / 721 / 1155, Uniswap V3 / V4 pools, Hardhat, Foundry, Web3.js. Attestations as cheap events + calldata, not a novel L1 religion.

**Avalanche** — C-Chain contracts, subnets when isolation is the point, bridges when it is not.

**Polkadot** — Substrate, parachains, XCM. Herd state as a runtime pallet is the long game, not a tweet.

**Cardano** — Aiken, eUTxO, Plutus / Marlowe. Datum is the animal. Redeemer is the proof the collar still exists.

**Sui** — Move object model, zkLogin, sponsored txns. A collar is an object. A ping mutates it. A sponsor pays the farmer's gas.

**Currently in the lab** — Substrate internals, Move resource safety, ZK proofs. Learning in public, breaking things on purpose.

</details>

---

### `$ ls /usr/local/bin`

<img src="./assets/bin.svg" width="100%" alt="toolchain listing" />

<div align="center">

**userspace**

<img src="https://skillicons.dev/icons?i=react,nextjs,typescript,javascript,html,css,tailwind,figma,nodejs,python,django,graphql,mysql,postgresql,firebase,docker,linux,git&theme=dark" alt="userspace toolchain" />

**kernel-adjacent**

<img src="https://img.shields.io/badge/Solidity-0b0a09?style=for-the-badge&logo=solidity&logoColor=c4a574" alt="Solidity" />
<img src="https://img.shields.io/badge/Foundry-0b0a09?style=for-the-badge&logo=ethereum&logoColor=e85d04" alt="Foundry" />
<img src="https://img.shields.io/badge/Hardhat-0b0a09?style=for-the-badge&logo=ethereum&logoColor=f4efe6" alt="Hardhat" />
<img src="https://img.shields.io/badge/Ethereum-0b0a09?style=for-the-badge&logo=ethereum&logoColor=627EEA" alt="Ethereum" />
<img src="https://img.shields.io/badge/Uniswap-0b0a09?style=for-the-badge&logo=uniswap&logoColor=FF007A" alt="Uniswap" />
<img src="https://img.shields.io/badge/Avalanche-0b0a09?style=for-the-badge&logo=avalanche&logoColor=E84142" alt="Avalanche" />
<img src="https://img.shields.io/badge/Polkadot-0b0a09?style=for-the-badge&logo=polkadot&logoColor=E6007A" alt="Polkadot" />
<img src="https://img.shields.io/badge/Cardano-0b0a09?style=for-the-badge&logo=cardano&logoColor=0033AD" alt="Cardano" />
<img src="https://img.shields.io/badge/Aiken-0b0a09?style=for-the-badge&logo=cardano&logoColor=00C2FF" alt="Aiken" />
<img src="https://img.shields.io/badge/Sui_Move-0b0a09?style=for-the-badge&logo=sui&logoColor=4DA2FF" alt="Sui" />
<img src="https://img.shields.io/badge/Web3.js-0b0a09?style=for-the-badge&logo=web3dotjs&logoColor=F16822" alt="Web3.js" />
<img src="https://img.shields.io/badge/ZK-warming_up-0b0a09?style=for-the-badge&logo=zeromq&logoColor=7dd3a0" alt="ZK" />

</div>

---

### `$ git log --stat`

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=mokayaj857&count_private=true&show_icons=true&theme=transparent&hide_border=true&title_color=e85d04&icon_color=c4a574&text_color=d6d3d1&rank_icon=github" alt="GitHub stats" />
  <img height="165" src="https://streak-stats.demolab.com/?user=mokayaj857&theme=transparent&hide_border=true&ring=e85d04&fire=c4a574&currStreakLabel=c4a574&currStreakNum=f4efe6&sideLabels=c4a574&sideNums=d6d3d1&dates=a8a29e" alt="Streak" />
  <br/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=mokayaj857&hide=HTML&langs_count=8&layout=compact&theme=transparent&hide_border=true&title_color=e85d04&text_color=d6d3d1" alt="Top languages" />
</div>

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=mokayaj857&bg_color=0b0a09&color=c4a574&line=e85d04&point=7dd3a0&area=true&hide_border=true" width="100%" alt="contribution activity graph" />

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mokayaj857/mokayaj857/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mokayaj857/mokayaj857/output/github-contribution-grid-snake.svg" />
    <img alt="snake on the contribution grid because of course" src="https://raw.githubusercontent.com/mokayaj857/mokayaj857/output/github-contribution-grid-snake.svg" />
  </picture>
</div>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=mokayaj857&theme=onestar&no-frame=true&no-bg=true&rank=-C,-B&column=6&margin-w=10&margin-h=8" alt="trophies" />
</div>

---

### `$ crontab -l`

```cron
# m h  dom mon dow  command
  0 *  *   *   *   ping collar || page watchtower
  @reboot          compile contracts && index heads
  0 2  *   *   *   study substrate / move / zk
  * *  *   *   *   be open to weird, serious collaboration
```

<p align="center">
  <a href="https://ko-fi.com/V7V4RAK9C"><img height="36" src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Ko-fi" /></a>
</p>

```
     ^__^                    48 45 52 44
     (oo)\_______            tag 0x0857
     (__)\       )\/\        lat -1.286389
         ||----w |           lng  36.817223
         ||     ||           proof != rumour
```

<img src="./assets/close.svg" width="100%" alt="If the animal moves, the chain should know." />
